from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
from django.views.generic.edit import FormView
from utility.forms import UserForm, ProfileForm, DepartmentForm, SectionForm, ImportFileForm
from utility.models import ProfileUtility, Department, Section
from workOrder.models import Status
import pandas as pd

# Create your views here.
@login_required
def index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'indexUtility.html')

class ProfileUpdateView(LoginRequiredMixin, TemplateView):

    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'utility\profile.html'

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

class DepartmentCreate(LoginRequiredMixin, CreateView):

    form_class = DepartmentForm
    model = Department
    template_name = 'utility/DepartmentForm.html'  # Specify your own template name/location

    # Sending user object to the form, to verify which fields to display/remove (depending on group)
    def get_form_kwargs(self):
        kwargs = super(DepartmentCreate, self).get_form_kwargs()

        return kwargs

    def get_initial(self):        
        initial = super(DepartmentCreate, self).get_initial()

        return initial
        # now the form will be shown with the link_pk bound to a value

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DepartmentCreate,self).get_context_data(**kwargs)

        return context

    def form_valid(self, form,**kwargs):
        self.object = form.save(commit=False)

        self.object.save()

        return super(DepartmentCreate,self).form_valid(form)    

class SectionCreate(LoginRequiredMixin, CreateView):

    form_class = SectionForm
    model = Section
    template_name = 'utility/SectionForm.html'  # Specify your own template name/location

    # Sending user object to the form, to verify which fields to display/remove (depending on group)
    def get_form_kwargs(self):
        kwargs = super(SectionCreate, self).get_form_kwargs()

        return kwargs

    def get_initial(self):        
        initial = super(SectionCreate, self).get_initial()

        return initial
        # now the form will be shown with the link_pk bound to a value

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SectionCreate,self).get_context_data(**kwargs)

        return context

    def form_valid(self, form,**kwargs):
        self.object = form.save(commit=False)

        self.object.save()

        return super(SectionCreate,self).form_valid(form)    

class ImportFileFormView(FormView):
    template_name = 'utility/ImportFileForm.html'
    form_class = ImportFileForm
    success_url = '/utility/config/import/'

    #buffer context
    plus_context = {}

    def get_initial(self):
        initial = super(ImportFileFormView, self).get_initial()
        file_name = 'cmmsConfig.xls'

        #get parameter from request.POST parameters, and put default value if none 'key': 
        initial['file_name'] = self.plus_context.get('file_name', file_name)
        #print(f"initial['file_name'] : {initial['file_name']}")

        return initial
        # now the form will be shown with the link_pk bound to a value

    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)

        #restore previous value
        context['file_name'] = self.plus_context.get('file_name', 'file_name')
        file_name = context['file_name']

        isFileAvailable = self.plus_context.get('isFileAvailable', False)
        if isFileAvailable:
            self.plus_context['isFileAvailable'] = False
            context['dataDict']=self.plus_context.get('dataDict','No data')
            context['countBefore'] = Status.objects.all().count()
            context['countAfter']=self.plus_context.get('countAfter','No data')

        return context

    def form_valid(self, form,**kwargs):

        #get data from form 
        file_name = form.cleaned_data.get('file_name')

        if 'read_file' in self.request.POST:
            if len(file_name):
                dataDict = self.readFile(file_name, 'status')

                #persistance previous value
                self.plus_context['isFileAvailable'] = True
                self.plus_context['file_name'] = file_name
                self.plus_context['dataDict'] = dataDict

        elif 'save_database' in self.request.POST:
            self.savaUpdateDatabase()

        return super(ImportFileFormView,self).form_valid(form)    

    def readFile(self, file_name, sheet_name):
        dataFrame = pd.read_excel(file_name, sheet_name)
        dataDict = dataFrame.to_dict()

        #display - print dict
        # self.__showDict(dataDict)

        return (dataDict)

    def __showDict(self, dictDta):        
        '''show 2D dictionary'''
        headStr = ''
        for head in self.__getFields(dictDta):
            if headStr == '':
                headStr = f'{head}'
            else:
                headStr += f',{head}'
        print(headStr)

        dataList = self.__toList(dictDta)
        fieldNbr = len(dataList)
        rowNbr = len(dataList[0])
        for row in range(rowNbr):
            for fld in range (fieldNbr):
                if fld == 0:
                    rowData = f'{dataList[fld][row]}'
                else:
                    rowData += f',{dataList[fld][row]}'
            print(rowData)

    def __getFields(self, dictData):
        '''get fields of 2D dictionary'''
        fields =[]
        for field in dictData.keys():
            fields.append(field)        
        return fields

    def __toList(self, dictData):
        '''get row data of 2D dictionary'''
        dataList=[]
        rowData =[]
        for field in dictData.keys():
            for row in dictData.get(field):
                rowData.append(dictData.get(field).get(row))
            
            #use copy for avoid resetting data
            dataList.append(rowData.copy())
            
            #reset/clear data, after saving
            rowData.clear()
        return dataList

    def __getRowData(self, dictData, row):
        '''get row data of 2D dictionary'''
        rowData =[]
        for field in dictData.keys():
            rowData.append(dictData.get(field).get(row))
        return rowData

    def savaUpdateDatabase(self):
        dataDict = self.plus_context.get('dataDict','No data')
        sts = Status.objects.all()

        for row in range(dataDict.shape[0]):
            name = dataDict.loc[row].at['name']
            description = dataDict.loc[row].at['description']

            #check if name is exist
            #sts.filter(name=name)
            obj, created = Status.objects.update_or_create(
                name=name,
                defaults={'description': description},
            )

        self.plus_context['countAfter'] = Status.objects.all().count()
