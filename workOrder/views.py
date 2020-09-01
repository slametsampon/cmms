from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import datetime

from django import forms
from workOrder.forms import WoJournalForm, UserForm, ProfileForm
from workOrder.forms import WoCompletion_form
from workOrder.models import Work_order, Work_order_journal, Work_order_completion
from workOrder.generals import WoMisc as WM

@login_required
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    #num_work_orders = Work_order.objects.all().count()
    woOnConcern = Work_order.objects.all().filter(current_user_id=request.user.id).count()
    
    context = {
        'woNwoOnConcernumber': woOnConcern,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class Work_orderListView(LoginRequiredMixin, generic.ListView):
    model = Work_order #prinsipnya dengan ini saja sdh cukup, namun kita perlu tambahan info di bawah ini
    context_object_name = 'user_work_order_list'   # your own name for the list as a template variable
    template_name = 'workOrder/user_work_order_list.html'  # Specify your own template name/location

    def get_queryset(self):
        self.wm = WM(self.request.user)
        
        #get wo concern base on pk list
        return Work_order.objects.filter(pk__in=self.wm.woOnCurrentUser())

class Work_orderDetailView(LoginRequiredMixin, generic.DetailView):
    model = Work_order #prinsipnya dengan ini saja sdh cukup, namun kita perlu tambahan info di bawah ini

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Add in a QuerySet of journal for history listing
        context['woPK'] = context['object'].id
        context['journal_list'] = Work_order_journal.objects.filter(wO_on_process=context['object'].id)
        return context

class Work_orderCreate(LoginRequiredMixin, CreateView):
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

class Work_orderUpdate(LoginRequiredMixin, UpdateView):
    model = Work_order
    fields = '__all__'
    template_name = 'workOrder/work_order_form.html'  # Specify your own template name/location

class Work_orderForward(LoginRequiredMixin, CreateView):
    form_class = WoJournalForm
    model = Work_order_journal
    template_name = 'workOrder/WoJournal_form.html'  # Specify your own template name/location

    # Sending user object to the form, to verify which fields to display/remove (depending on group)
    def get_form_kwargs(self):
        kwargs = super(Work_orderForward, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_initial(self):        
        initial = super(Work_orderForward, self).get_initial()

        return initial
        # now the form will be shown with the link_pk bound to a value

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Work_orderForward,self).get_context_data(**kwargs)
        woOnProcess = Work_order.objects.get(id=self.kwargs.get("pk"))

        # Add object in context wo_number use for woHeader.html
        context['work_order'] = woOnProcess

        return context

    def form_valid(self, form,**kwargs):
        self.wm = WM(self.request.user)
        self.object = form.save(commit=False)

        #set work_order_journal date - done by program
        self.object.date = datetime.date.today()

        #set work_order_journal time - done by program
        self.object.time = datetime.datetime.now().time()

        #set concern_user date_open
        self.object.concern_user = self.request.user

        #get wO_on_process - done by program
        wO_on_process = Work_order.objects.get(id=self.kwargs.get("pk"))

        #set work_order  - done by program
        self.object.wO_on_process = wO_on_process

        self.object.save()

        #get data from form
        action = form.cleaned_data.get('action')

        #complete role is special case since, all data Work order available in this area
        if action == 't': #complete
            #get id Originator
            current_user_id = wO_on_process.originator.id
            #wO_completed.updateExecutorUserId(self.request.user.id)
        else:
            current_user_id = self.wm.getCurrentUser(action).id

        #update current_user_id
        wO_on_process.updateCurrentUserId(current_user_id)

        #update status work order 
        status = self.wm.getWoStatus(action)
        wO_on_process.updateStatus(status)

        return super(Work_orderForward,self).form_valid(form)    

class WoCompletion(LoginRequiredMixin, CreateView):

    form_class = WoCompletion_form
    model = Work_order_completion
    template_name = 'workOrder/WoCompletion_form.html'  # Specify your own template name/location

    # Sending user object to the form, to verify which fields to display/remove (depending on group)
    def get_form_kwargs(self):
        kwargs = super(WoCompletion, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_initial(self):        
        initial = super(WoCompletion, self).get_initial()

        return initial
        # now the form will be shown with the link_pk bound to a value

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(WoCompletion,self).get_context_data(**kwargs)
        wO_completed = Work_order.objects.get(id=self.kwargs.get("pk"))

        # Add object in context wo_number use for woHeader.html
        context['work_order'] = wO_completed

        # Add object in context date_open use in form
        context['date'] = datetime.date.today()

        return context

    def form_valid(self, form,**kwargs):
        self.wm = WM(self.request.user)
        self.object = form.save(commit=False)

        #set date - done by program
        self.object.date = datetime.date.today()

        #set acted_user - done by program
        self.object.acted_user = self.request.user

        #set wO_completed - done by program
        wO_completed = Work_order.objects.get(id=self.kwargs.get("pk"))
        self.object.wO_completed = wO_completed

        self.object.save()

        #get data from form, status also as action 
        action = form.cleaned_data.get('status')

        #finish role is special case since, all data Work order available in this area
        if action == 'h': #finish
            wO_completed.updateExecutorUserId(self.request.user.id)
            wO_completed.updateDateFinish(datetime.date.today())

        #update work order current_user_id
        current_user_id = self.wm.getCurrentUser(action).id
        wO_completed.updateCurrentUserId(current_user_id)

        #update status work order
        status = self.wm.getWoStatus(action)
        wO_completed.updateStatus(status)

        return super(WoCompletion,self).form_valid(form)    

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