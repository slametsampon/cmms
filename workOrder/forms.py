from django import forms
from django.forms import ModelForm, Select
from django.contrib.auth.models import User
from workOrder.models import Wo_journal, Wo_completion, Work_order, Wo_instruction
from utility.models import Profile, Wo_priority, CategoryAction
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import datetime

class work_order_form(ModelForm):

   def clean_tagnumber(self):
      data = self.cleaned_data['tagnumber']
      
      # Remember to always return the cleaned data.
      return data

   def clean_problem(self):
      data = self.cleaned_data['problem']
      
      # Remember to always return the cleaned data.
      return data

   def clean_priority(self):
      data = self.cleaned_data['priority']
      
      # Remember to always return the cleaned data.
      return data

   def clean_dest_section(self):
      data = self.cleaned_data['dest_section']
      
      # Remember to always return the cleaned data.
      return data

   def __init__(self, *args, **kwargs):
      #self.user = kwargs.pop('user') #take current user
      super(work_order_form, self).__init__(*args, **kwargs)

      self.fields['tagnumber'].widget = forms.TextInput()
      self.fields['problem'].widget = forms.Textarea(attrs={'rows':3})

   class Meta:
      template_name = 'workOrder/WoCompletion_form.html'  # Specify your own template name/location

      model = Work_order
      fields = ['tagnumber',
                  'problem',
                  'priority',
                  'dest_section',
               ]

class WoJournalForm(ModelForm):

   def clean_comment(self):
      data = self.cleaned_data['comment']
      
      # other check logic if needed
      # Remember to always return the cleaned data.
      return data
   
   def clean_action(self):
      data = self.cleaned_data['action']
      
      # other check logic if needed
      # Remember to always return the cleaned data.
      return data

   def __init__(self, *args, **kwargs):

      self.user = kwargs.pop('user')
      super(WoJournalForm, self).__init__(*args, **kwargs)
      #get actions from Profile - user
      actDict = {}
      for action in Profile.objects.get(user=self.user).actions.all():
         actDict[action.pk] = action.name

      # Converting into list of tuple 
      actlist = list(actDict.items()) 
      actions = Profile.objects.get(user=self.user).actions.all()               
      self.fields['action'].widget = Select(choices=actlist)

   class Meta:
      template_name = 'workOrder/WoJournal_form.html'  # Specify your own template name/location

      model = Wo_journal
      fields = ['comment',
                  'action']

      labels = {'comment': _('comment')}
      widgets = { 'comment': forms.Textarea(attrs={'rows':3})}
      labels = {'action': _('action')}

class WoInstruction_form(ModelForm):

    def clean_instruction(self):
       data = self.cleaned_data['instruction']
       
       # other check logic if needed
       # Remember to always return the cleaned data.
       return data
    
    def __init__(self, *args, **kwargs):

        self.user = kwargs.pop('user')
        super(WoInstruction_form, self).__init__(*args, **kwargs)

    class Meta:
        template_name = 'workOrder/WoInstruction_form.html'  # Specify your own template name/location

        model = Wo_instruction
        fields = [
           'instruction',
            ]

        widgets = { 'instruction': forms.Textarea(attrs={'rows':5})}

class WoCompletion_form(ModelForm):

   def clean_status(self):
      data = self.cleaned_data['status']
      
      # Remember to always return the cleaned data.
      return data

   def clean_activity(self):
      data = self.cleaned_data['activity']
      
      # Remember to always return the cleaned data.
      return data

   def clean_manPower(self):
      data = self.cleaned_data['manPower']
      
      # Remember to always return the cleaned data.
      return data

   def clean_duration(self):
      data = self.cleaned_data['duration']
      
      # other check logic if needed
      if data <= 0:
         raise ValidationError(_('Invalid duration - can not zero/minus'))

      # Remember to always return the cleaned data.
      return data

   def clean_material(self):
      data = self.cleaned_data['material']
      
      # Remember to always return the cleaned data.
      return data

   def clean_tool(self):
      data = self.cleaned_data['tool']
      
      # Remember to always return the cleaned data.
      return data

   def __init__(self, *args, **kwargs):
      self.user = kwargs.pop('user') #take current user
      super(WoCompletion_form, self).__init__(*args, **kwargs)

      #get actions from Profile - user
      actDict = {}
      for action in Profile.objects.get(user=self.user).actions.all():
         actDict[action.pk] = action.name

      # Converting into list of tuple 
      actlist = list(actDict.items()) 
      self.fields['status'].widget = Select(choices=actlist)

   class Meta:
      template_name = 'workOrder/WoCompletion_form.html'  # Specify your own template name/location

      model = Wo_completion
      fields = [
         'status',
         'manPower',
         'duration',
         'activity',
         'material',
         'tool',
         ]
      widgets = { 
         'manPower': forms.Textarea(attrs={'rows':1}),
         'activity': forms.Textarea(attrs={'rows':4}),
         'tool': forms.Textarea(attrs={'rows':4}),
         'material': forms.Textarea(attrs={'rows':4}),
         }

from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})
class WoSummaryReportForm(forms.Form):

   catDict = {}
   for cat in CategoryAction.objects.all():
      catDict[cat.name] = cat.name

   #add one more for Incoming
   catDict['Incoming'] = 'Incoming'

   # Converting into list of tuple 
   catlist = list(catDict.items()) 

   start_date = forms.DateField(widget=DateInput())
   end_date = forms.DateField(widget=DateInput())
   wo_category = forms.CharField(widget=Select(choices=catlist))

   def clean_start_date(self):
      data = self.cleaned_data['start_date']
      
      # other check logic if needed
      # Remember to always return the cleaned data.
      return data

   def clean_end_date(self):
      data = self.cleaned_data['end_date']
      
      # other check logic if needed
      # Remember to always return the cleaned data. datetime.timedelta(days=30)
      return data

   def clean_wo_status(self):
      data = self.cleaned_data['wo_status']
      
      # other check logic if needed
      # Remember to always return the cleaned data. datetime.timedelta(days=30)
      return data

class WoReportForm(forms.Form):

    class Meta:
        template_name = 'workOrder/WoReport_form.html'  # Specify your own template name/location
