import datetime
from django.shortcuts import render

from workOrder.models import Work_order, Work_order_journal
from workOrder.generals import WoMisc as WM

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

from django.contrib.auth import authenticate, login
def cmms_login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
    else:
        pass
        # Return an 'invalid login' error message.

from django.views import generic
class Work_orderListView(generic.ListView):
    model = Work_order #prinsipnya dengan ini saja sdh cukup, namun kita perlu tambahan info di bawah ini
    context_object_name = 'user_work_order_list'   # your own name for the list as a template variable
    template_name = 'workOrder/user_work_order_list.html'  # Specify your own template name/location

    def get_queryset(self):
        self.wm = WM(self.request.user)
        
        #get wo concern base on pk list
        return Work_order.objects.filter(pk__in=self.wm.woOnCurrentUser())

class Work_orderDetailView(generic.DetailView):
    model = Work_order #prinsipnya dengan ini saja sdh cukup, namun kita perlu tambahan info di bawah ini

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Add in a QuerySet of journal
        context['woPK'] = context['object'].id
        context['journal_list'] = Work_order_journal.objects.filter(wO_on_process=context['object'].id)
        return context

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class Work_orderCreate(CreateView):
    model = Work_order
    template_name = 'workOrder/work_order_form.html'  # Specify your own template name/location
    fields = ['tagnumber',
                'problem',
                'priority',
                'dest_section']

    def get_context_data(self, **kwargs):
        self.wm = WM(self.request.user)
        # Call the base implementation first to get a context
        context = super(Work_orderCreate,self).get_context_data(**kwargs)

        # Add object in context wo_number
        context['wo_number'] = self.wm.getWoNumber()

        # Add object in context date_open
        context['date_open'] = datetime.date.today()

        # Add object in context originator
        context['originator'] = self.request.user

        #set work_order status
        context['status'] = self.wm.getWoStatus('f') #forward
        #print(f'get_context_data=>context : {context}')

        return context

    def form_valid(self, form,**kwargs):
        self.wm = WM(self.request.user)
        self.object = form.save(commit=False)
        #context = super(Work_orderCreate,self).get_context_data(**kwargs)
        #print(f'form_valid=>context : {context}')

        #set work_order date_open
        self.object.date_open = datetime.date.today()

        #set work_order wo_number
        self.object.wo_number = self.wm.getWoNumber()

        #set work_order originator
        self.object.originator = self.request.user

        #set work_order status
        self.object.status = self.wm.getWoStatus('f') #forward

        #getApprover
        approver = self.wm.getCurrentUser('f') #forward

        #set current_user_id 
        self.object.current_user_id = approver.id

        self.object.save()

        #set init journal for every first opening work order
        self.wm.woInitJournal()

        return super(Work_orderCreate,self).form_valid(form)    

class Work_orderUpdate(UpdateView):
    model = Work_order
    fields = '__all__'
    template_name = 'workOrder/work_order_form.html'  # Specify your own template name/location

from django import forms
class Work_orderForward(CreateView):
    model = Work_order_journal
    fields = ['comment',
                'action']

    template_name = 'workOrder/WoJournal_form.html'  # Specify your own template name/location

    ACTION_STATUS = (
        ('f', 'Forward'),
        ('r', 'Return'),
        ('o', 'Other'),
    )

    def get_initial(self):
        initial = super(Work_orderForward, self).get_initial()

        #put some choices dynamicaly
        #self.fields['action'] = forms.ChoiceField(choices=self.ACTION_STATUS)

        return initial
        # now the form will be shown with the link_pk bound to a value

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Work_orderForward,self).get_context_data(**kwargs)
        woNumber = Work_order.objects.get(id=self.kwargs.get("pk")).wo_number

        # Add object in context wo_number
        context['wO_on_process'] = woNumber

        # Add object in context date_open
        context['date'] = datetime.date.today()

        return context

    def form_valid(self, form,**kwargs):
        self.wm = WM(self.request.user)
        self.object = form.save(commit=False)

        #set work_order_journal date
        self.object.date = datetime.date.today()

        #set work_order_journal date
        self.object.time = datetime.date.today().time()

        #set concern_user date_open
        self.object.concern_user = self.request.user

        #get wO_on_process
        wO_on_process = Work_order.objects.get(id=self.kwargs.get("pk"))

        #set work_order wo_number
        self.object.wO_on_process = wO_on_process

        self.object.save()

        #update status work order and current_user_id
        action = form.cleaned_data.get('action')

        current_user_id = self.wm.getCurrentUser(action).id
        status = self.wm.getWoStatus(action)
        wO_on_process.updateStatus(status)
        wO_on_process.updateCurrentUserId(current_user_id)

        return super(Work_orderForward,self).form_valid(form)    

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