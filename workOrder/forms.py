from django.forms import ModelForm, Select
from django.contrib.auth.models import User
from workOrder.models import Profile, Work_order_journal

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','password')

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

from django.utils.translation import gettext_lazy as _
class WoJournalForm(ModelForm):
    def __init__(self, *args, **kwargs):
        ACTIONS = (
            ('f', 'Forward'),
            ('r', 'Return'),
        )
        self.user = kwargs.pop('user')
        super(WoJournalForm, self).__init__(*args, **kwargs)

        #selesct form ACTIONS as user
        print(f'self.user.username:{self.user.username}')
        if self.user.username == 'sptdExe':
            ACTIONS = (
                ('f', 'Forward'),
                ('r', 'Return'),
                ('s', 'Shutdown'),
                ('l', 'Need Materials'),
                ('m', 'Need MOC'),
            )
        
        self.fields['action'].widget = Select(choices=ACTIONS)

    class Meta:
        template_name = 'workOrder/WoJournal_form.html'  # Specify your own template name/location

        model = Work_order_journal
        fields = ['comment',
                    'action']

        labels = {'comment': _('comment')}
        #help_texts = {'comment': _('Enter comment')} 

        labels = {'action': _('action')}
        #help_texts = {'action': _('Select action')} 
        #widgets = {'action': Select(choices=ACTIONS)}

class WoJournalGeneralUserForm(ModelForm):
    class Meta:
        ACTIONS = (
            ('f', 'Forward'),
            ('r', 'Return'),
        )
        template_name = 'workOrder/WoJournal_form.html'  # Specify your own template name/location

        model = Work_order_journal
        fields = ['comment',
                    'action']

        labels = {'comment': _('comment')}
        #help_texts = {'comment': _('Enter comment')} 

        labels = {'action': _('action')}
        #help_texts = {'action': _('Select action')} 
        widgets = {'action': Select(choices=ACTIONS)}

        