from django import forms
from product.models import Plan,Features
class Customer_form(forms.ModelForm):
    class Meta:
        model = Customer
        fields= ['name'
            ,'phone_no'
            ,'email'
            ,'address'
            ,'profile_picture'
            ,'verified_type']
    def __init__(self, *args, **kwargs):
        super(Customer_form, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter name'
        self.fields['phone_no'].widget.attrs['placeholder'] = 'Enter phone_no'        
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email'
        self.fields['verified_type'].widget.attrs['placeholder'] = 'Enter verified_type'
        self.fields['address'].widget.attrs['placeholder'] = 'Enter address'