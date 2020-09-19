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
from django.contrib.auth.models import User
import pandas as pd
from xlrd import open_workbook
from cmms import settings 

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

    MODEL = (
        (0,'Department'),
        (1,'Section'),
        (2,'Action'),
        (3,'User'),
        (4,'ProfileUtility'),
        (5,'ProfileAction'),
    )
    #buffer context
    plus_context = {}

    def get_initial(self):
        initial = super(ImportFileFormView, self).get_initial()

        #get parameter from request.POST parameters, and put default value if none 'key': 
        initial['file_name'] = self.plus_context.get('file_name', None)
        #print(f"initial['file_name'] : {initial['file_name']}")

        return initial
        # now the form will be shown with the link_pk bound to a value

    # Sending user object to the form, to verify which fields to display/remove (depending on group)
    def get_form_kwargs(self):
        kwargs = super(ImportFileFormView, self).get_form_kwargs()
        kwargs.update({'sheetNames': self.plus_context.get('sheetNames', None)})
        kwargs.update({'modelNames': self.plus_context.get('modelNames', None)})
        kwargs.update({'sheet_index': self.plus_context.get('sheet_index', 0)})
        kwargs.update({'model_index': self.plus_context.get('model_index', 0)})
        return kwargs

    def get_context_data(self, **kwargs):
        self.plus_context['modelNames'] = self.MODEL

        # Call the base implementation first to get a context self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)

        #restore previous value
        context['file_name'] = self.plus_context.get('file_name', None)
        context['sheetNames'] = self.plus_context.get('sheetNames', [])
        context['modelNames'] = self.plus_context.get('modelNames', [])

        isFileAvailable = self.plus_context.get('isFileAvailable', False)
        if isFileAvailable:
            self.plus_context['isFileAvailable'] = False
            context['dataDict']=self.plus_context.get('dataDict',None)
            context['countBefore'] = Status.objects.all().count()
            context['countAfter']=self.plus_context.get('countAfter',None)

        return context

    def form_valid(self, form,**kwargs):

        #get data from form 
        file_name = form.cleaned_data.get('file_name')
        model_index = form.cleaned_data.get('model_index')
        sheet_index = form.cleaned_data.get('sheet_index')

        #persistance previous value
        self.plus_context['sheet_index'] = sheet_index
        self.plus_context['model_index'] = model_index

        if not file_name:
            file_name = self.plus_context.get('file_name', None)

        if 'open_file' in self.request.POST:
            if len(file_name):
                self.plus_context['file_name'] = file_name
                self.plus_context['sheetNames'] = self.openFile(file_name)

        elif 'read_file' in self.request.POST:
            if len(file_name):
                #persistance previous value
                self.plus_context['isFileAvailable'] = True
                self.plus_context['dataDict'] = self.readFile(file_name, sheet_index)

        elif 'save_database' in self.request.POST:
            self.savaUpdateDatabase(model_index)

        return super(ImportFileFormView,self).form_valid(form)    

    def openFile(self, file_name):
        sheetList =[]
        
        file_name = f'{settings.MEDIA_ROOT}\{file_name}'
        book = open_workbook(file_name)
        sheetNames = book.sheet_names()

        if sheetNames:
            sheetDict ={}
            i=0
            for sheet in sheetNames:
                sheetDict[i]=sheet
                i+=1
            # Converting into list of tuple 
            sheetList = list(sheetDict.items())

        return sheetList

    def readFile(self, file_name, sheet_index):

        #get list of tuple
        file_name = f'{settings.MEDIA_ROOT}\{file_name}'
        sheet_name = self.plus_context.get('sheetNames')

        sheetIdx = sheet_name[sheet_index]
        sheet = sheetIdx[1]

        dataFrame = pd.read_excel(file_name, sheet)
        dataDict = dataFrame.to_dict()

        # self.__showDict(dataDict)
        # print(self.__toPairDict(dataDict))
        
        return (dataDict)

    def savaUpdateDatabase(self,model_index):
        modelIdx = self.MODEL[model_index]
        modelName = modelIdx[1]

        dataDict = self.plus_context.get('dataDict',None)
        if modelName == 'Department':
            for dtDict in self.__toPairDict(dataDict):

                #update_or_create for first field as unique value
                obj, created = Department.update_or_create_dict(dtDict)            
            self.plus_context['countAfter'] = Department.objects.all().count()

        elif modelName == 'Section':
            for dtDict in self.__toPairDict(dataDict):
                
                #update_or_create for first field as unique value
                obj, created = Section.update_or_create_dict(dtDict)            
            self.plus_context['countAfter'] = Section.objects.all().count()

        elif modelName == 'Action':
            for dtDict in self.__toPairDict(dataDict):

                #update_or_create for first field as unique value
                obj, created = Status.update_or_create_dict(dtDict)            
            self.plus_context['countAfter'] = Status.objects.all().count()

        elif modelName == 'User':
            for dtDict in self.__toPairDict(dataDict):
                k=None
                for k,v in dtDict.items():
                    if k:
                        break
                #username as unique value
                obj, created = User.objects.update_or_create(
                    username=v,
                    defaults=dtDict,
                )    
            self.plus_context['countAfter'] = User.objects.all().count()

        elif modelName == 'ProfileUtility':
            for dtDict in self.__toPairDict(dataDict):

                #update_or_create for first field as unique value
                obj, created = ProfileUtility.update_or_create_dict(dtDict)            
            self.plus_context['countAfter'] = ProfileUtility.objects.all().count()

        elif modelName == 'ProfileAction':
            print('ProfileAction')
            for dtDict in self.__toPairDict(dataDict):
                
                #update_or_create_action_dict
                ProfileUtility.update_or_create_action_dict(dtDict)            
            self.plus_context['countAfter'] = ProfileUtility.objects.all().count()


    def __showDict(self, dictDta):        
        '''show 2D dictionary'''
        headStr = ''
        for head in self.__getFields(dictDta):
            if headStr == '':
                headStr = f'{head}'
            else:
                headStr += f',{head}'
        #display header/fields
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
            #display data each row
            print(rowData)

    def __getFields(self, dictData):
        '''get fields of 2D dictionary, return list'''
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
        '''get row data of 2D dictionary, return list'''
        rowData =[]
        for field in dictData.keys():
            rowData.append(dictData.get(field).get(row))
        return rowData

    def __toPairDict(self,dictData):
        listPair=[]
        rowDict ={}
        dataList = self.__toList(dictData)
        fields = self.__getFields(dictData)
        rows = len(dataList[len(fields)-1])
        for row in range(rows):
            for fld in range(len(fields)):
                rowDict[fields[fld]]=dataList[fld][row]
            listPair.append(rowDict.copy())
        
        return listPair

