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
    images = forms.ImageField(required=True)
    
    def clean_images(self):
        images = self.cleaned_data.get('images')
        if isinstance(images, list) and len(images) < 20:
            raise forms.ValidationError("You must upload at least 20 images.")
        return images