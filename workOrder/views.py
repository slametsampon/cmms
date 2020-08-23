import datetime
from django.shortcuts import render

from workOrder.models import Work_order

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    #num_work_orders = Work_order.objects.all().count()
    num_work_orders = Work_order.objects.all().filter(originator=request.user.id).count()
    
    context = {
        'num_work_orders': num_work_orders,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class Work_orderListView(generic.ListView):
    model = Work_order

class Work_orderDetailView(generic.DetailView):
    model = Work_order

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from workOrder.generals import WoMisc as WM

class Work_orderCreate(CreateView):
    model = Work_order
    fields = ['wo_number',
                'tagnumber',
                'problem',
                'priority',
                'dest_section',
                'date_open',
                'originator',
                'action']

    initial ={'date_open' : datetime.date.today(),
            }

    def get_initial(self):
        self.wm = WM(self.request.user)

        #set work_order originator
        self.initial['originator'] = self.request.user.id 

        #set work_order wo_number
        self.initial['wo_number'] = self.wm.getWoNumber() 

        return self.initial

    def form_valid(self, form):
        self.object = form.save(commit=False)

        #set work_order status
        self.object.status = self.wm.getWoStatus(self.object.action)

        #just inspect value
        print(f'self.object.originator:{self.object.originator}')

        self.object.save()
        return super(Work_orderCreate,self).form_valid(form)    

class Work_orderUpdate(UpdateView):
    model = Work_order
    fields = '__all__'

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from workOrder.forms import UserForm, ProfileForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'workOrder\profile.html'

    def post(self, request):

        post_data = request.POST or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return HttpResponseRedirect(reverse_lazy('user_profile_update'))

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)