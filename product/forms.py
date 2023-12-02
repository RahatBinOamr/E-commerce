
from django import forms
from django.contrib.auth.models import User
from UserProfile.models import UserProfile
from product.models import Review

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        widgets = {
            'username': forms.TextInput({'class': 'form-control'}),
            'email': forms.EmailInput({'class': 'form-control'}),
            'password': forms.PasswordInput({'class': 'form-control'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image',  'address', 'mobile_number']
        widgets = {
            'profile_image': forms.ClearableFileInput({'class': 'form-control-file'}),
            'address': forms.Textarea({'class': 'form-control'}),
            'mobile_number': forms.TextInput({'class': 'form-control'}),
            
        }
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment']

        widgets={
            'comment':forms.TextInput({'class': 'form-control'})
        }