from django import forms
from django.forms import ModelForm, Select
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import datetime
from utility.models import Profile, Department, Section

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','password')
        widgets = { 
            'first_name': forms.TextInput(attrs={'size':20}),
            'last_name': forms.TextInput(attrs={'size':20}),
            'email': forms.EmailInput(attrs={'size':50}),
            'password': forms.PasswordInput(attrs={'size':20}),
            }

class ProfileForm(ModelForm):
    class Meta:
        userDict = {}
        for usr in User.objects.all():
            userDict[usr.pk] = usr.username

        # Converting into list of tuple 
        userlist = list(userDict.items()) 
        
        model = Profile
        fields = '__all__'
        widgets = { 
            'nik': forms.TextInput(attrs={'size':10}),
            'initial': forms.TextInput(attrs={'size':3}),
            'forward_path': forms.Select(choices=userlist),
            'reverse_path': forms.Select(choices=userlist),
            }

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        widgets = { 
            'name': forms.TextInput(attrs={'size':30}),
            'initial': forms.TextInput(attrs={'size':5}),
            'description': forms.Textarea(attrs={'rows':2}),
            }

class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = '__all__'
        widgets = { 
            'name': forms.TextInput(attrs={'size':30}),
            'initial': forms.TextInput(attrs={'size':5}),
            'description': forms.Textarea(attrs={'rows':2}),
            }

class ImportFileForm(forms.Form):
    file_name = forms.FileField(widget=forms.FileInput(attrs={'accept':'.xls,.xlsx'}))
    sheet_index = forms.IntegerField(widget=forms.TextInput())
    model_index = forms.IntegerField(widget=forms.TextInput())

    def clean_file_name(self):
       data = self.cleaned_data['file_name']
       
       # Remember to always return the cleaned data.
       return data

    def clean_sheet_index(self):
       data = self.cleaned_data['sheet_index']
       
       # Remember to always return the cleaned data.
       return data

    def clean_model_index(self):
       data = self.cleaned_data['model_index']
       
       # Remember to always return the cleaned data.
       return data

    def __init__(self, *args, **kwargs):

        initSheet = 0
        initModel = 0
        sheetNames = kwargs.pop('sheetNames') #take sheetNames from view
        modelNames = kwargs.pop('modelNames') #take modelNames from view
        initSheet = kwargs.pop('sheet_index') #take modelNames from view
        initModel = kwargs.pop('model_index') #take modelNames from view

        super(ImportFileForm, self).__init__(*args, **kwargs)

        if not sheetNames:
            sheetNames = ((0,''),)
        if not modelNames:
            modelNames = ((0,''),)

        self.fields['sheet_index'].required = False
        self.fields['sheet_index'].widget = Select(choices=sheetNames)
        self.fields['sheet_index'].initial = initSheet

        self.fields['model_index'].required = False
        self.fields['model_index'].widget = Select(choices=modelNames)
        self.fields['model_index'].initial = initModel
    
    class Meta:
        template_name = 'utility/ImportFileForm.html'  # Specify your own template name/location

