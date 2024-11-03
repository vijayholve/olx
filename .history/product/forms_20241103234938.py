from django import forms
from .models import Product, ProductImage

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category', 'location', 'condition','state']
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # Adding placeholders
        self.fields['title'].widget.attrs['placeholder'] = 'Enter product title'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter product description'
        self.fields['price'].widget.attrs['placeholder'] = 'Enter product price'
        self.fields['category'].widget.attrs['placeholder'] = 'Select a category'
        self.fields['location'].widget.attrs['placeholder'] = 'Enter location'
        self.fields['condition'].widget.attrs['placeholder'] = 'Select condition'
        self.fields['state'].widget.attrs['placeholder'] = 'Select state'
class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']


class MultipleImagesForm(forms.Form):
    images = forms.ImageField(required=True)
    
    