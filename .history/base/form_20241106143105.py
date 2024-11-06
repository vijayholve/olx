from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from django import forms
class resigration_Form(UserCreationForm):
    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        
        # Adding placeholders for text fields
        self.fields['title'].widget.attrs['placeholder'] = 'Enter product title'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter product description'
        self.fields['price'].widget.attrs['placeholder'] = 'Enter product price'
        self.fields['location'].widget.attrs['placeholder'] = 'Enter location'
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2
  

