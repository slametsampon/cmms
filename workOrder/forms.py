from django import forms
from django.forms import ModelForm, Select
from django.contrib.auth.models import User
from workOrder.models import Profile, Work_order_journal, Work_order_completion
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import datetime

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','password')

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class WoJournalForm(ModelForm):

    def clean_comment(self):
       data = self.cleaned_data['comment']
       
       # other check logic if needed
       #if data < datetime.date.today():
       #    raise ValidationError(_('Invalid date - renewal in past'))

       # Remember to always return the cleaned data.
       return data
    
    def clean_action(self):
       data = self.cleaned_data['action']
       
       # other check logic if needed
       #if data < datetime.date.today():
       #    raise ValidationError(_('Invalid date - renewal in past'))

       # Remember to always return the cleaned data.
       return data

    def __init__(self, *args, **kwargs):
        ACTIONS = (
            ('f', 'Forward'),
            ('r', 'Return'),
        )
        self.user = kwargs.pop('user')
        super(WoJournalForm, self).__init__(*args, **kwargs)

        #selesct form ACTIONS as user
        for g in self.user.groups.all():
            status = 'ot' #other

            #originator supervisor
            if 'ORG_SPV' == g.name:
                ACTIONS = (
                    ('f', 'Forward'),
                    ('c', 'Close'),
                )
            elif 'EXC_SPV' == g.name:
                ACTIONS = (
                    ('f', 'Forward'),
                    ('r', 'Return'),
                    ('c', 'Complete'),
                )
            elif 'EXC_SPTD' == g.name:
                ACTIONS = (
                    ('f', 'Forward'),
                    ('r', 'Return'),
                    ('s', 'Shutdown'),
                    ('l', 'Need Materials'),
                    ('m', 'Need MOC'),
                    ('o', 'Other'),
                )
        
        self.fields['action'].widget = Select(choices=ACTIONS)

    class Meta:
        template_name = 'workOrder/WoJournal_form.html'  # Specify your own template name/location

        model = Work_order_journal
        fields = ['comment',
                    'action']

        labels = {'comment': _('comment')}
        widgets = { 'comment': forms.Textarea(attrs={'rows':3})}
        #help_texts = {'comment': _('Enter comment')} 

        labels = {'action': _('action')}
        #help_texts = {'action': _('Select action')} 
        #widgets = {'action': Select(choices=ACTIONS)}

class WoCompletion_form(ModelForm):

    def clean_action(self):
       data = self.cleaned_data['action']
       
       # Remember to always return the cleaned data.
       print('WoCompletion_form:clean_action')
       return data

    def clean_manPower(self):
       data = self.cleaned_data['manPower']
       
       # Remember to always return the cleaned data.
       print('WoCompletion_form:clean_manPower')
       return data

    def clean_duration(self):
       data = self.cleaned_data['duration']
       
       # other check logic if needed
       if data <= 0:
           raise ValidationError(_('Invalid duration - can not zero/minus'))

       # Remember to always return the cleaned data.
       print('WoCompletion_form:clean_duration')
       return data

    def clean_material(self):
       data = self.cleaned_data['material']
       
       # Remember to always return the cleaned data.
       print('WoCompletion_form:clean_material')
       return data

    def clean_tool(self):
       data = self.cleaned_data['tool']
       
       # Remember to always return the cleaned data.
       print('WoCompletion_form:clean_tool')
       return data

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user') #take current user
        super(WoCompletion_form, self).__init__(*args, **kwargs)

    class Meta:
        template_name = 'workOrder/WoCompletion_form.html'  # Specify your own template name/location

        model = Work_order_completion
        fields = [
            'action',
            'manPower',
            'duration',
            'material',
            'tool',
            ]
        widgets = { 
            'manPower': forms.Textarea(attrs={'rows':2}),
            'action': forms.Textarea(attrs={'rows':5}),
            'tool': forms.Textarea(attrs={'rows':5}),
            'material': forms.Textarea(attrs={'rows':5}),
            }
