from django import forms
from product.models import Product
from ckeditor.fields import RichTextField

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'  
        widgets = {
            'product_title': forms.TextInput({'class': 'form-control'}),
            'product_current_price': forms.NumberInput({'class': 'form-control'}),
            'product_previous_price': forms.NumberInput({'class': 'form-control'}),
            'product_quantity': forms.NumberInput({'class': 'form-control'}),
            'product_rating': forms.NumberInput({'class': 'form-control'}),
            'product_offer': forms.NumberInput({'class': 'form-control'}),
            'product_description': RichTextField(),
            'product_image': forms.FileInput({'class': 'form-control'}),
            'product_category': forms.Select({'class': 'form-control'}),
            'product_status': forms.Select({'class': 'form-control'}),
            'product_brand': forms.Select({'class': 'form-control'}),
        }