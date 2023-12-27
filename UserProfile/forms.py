from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Profile

class RegistrationForm(UserCreationForm): 
    class Meta:
        model=User
        fields =['first_name', 'username', 'email', 'password1','password2']


class UpdateRegisterForm(forms.ModelForm):

    class Meta:
        model= User
        fields =[ 'username', 'first_name', 'email']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))    