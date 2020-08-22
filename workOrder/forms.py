from django.forms import ModelForm
from django.contrib.auth.models import User
from workOrder.models import Profile

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','password')

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


