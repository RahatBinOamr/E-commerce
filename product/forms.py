from django import forms
from UserProfile.models import Profile
from product.models import Review


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image',  'address', 'mobile_number']
        widgets = {
            'profile_image': forms.ClearableFileInput({'class': 'form-control-file'}),
            'address': forms.Textarea({'class': 'form-control'}),
            'mobile_number': forms.TextInput({'class': 'form-control'}),
            
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment']

        widgets={
            'comment':forms.TextInput({'class': 'form-control'})
        }