from django import forms
from .models import Product, ProductImage

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category', 'location', 'condition']

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image'] 

class MultipleImagesForm(forms.Form):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=True)
