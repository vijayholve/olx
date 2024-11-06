from django import forms
from .models import Product, ProductImage

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category', 'location', 'condition','state']
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        
        # Adding placeholders for text fields
        self.fields['title'].widget.attrs['placeholder'] = 'Enter product title'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter product description'
        self.fields['price'].widget.attrs['placeholder'] = 'Enter product price'
        self.fields['location'].widget.attrs['placeholder'] = 'Enter location'

        # Manually creating choices list for dropdowns
        self.fields['category'].choices = [('', 'Select a category')] + list(self.fields['category'].choices)
        self.fields['condition'].choices = [('', 'Select condition')] + list(self.fields['condition'].choices)
        self.fields['state'].choices = [('', 'Select state')] + list(self.fields['state'].choices)
class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']


class MultipleImagesForm(forms.Form):
    images = forms.ImageField(required=True)
    
    class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'date', 'status']  # Add fields you need for the transaction model

class YourOtherModelForm(forms.ModelForm):
    class Meta:
        model = YourOtherModel
        fields = ['field1', 'field2', 'field3']  # Include the fields from the model