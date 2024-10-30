from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django import forms
from django.contrib.auth.models import User 

class resigration_Form(UserCreationForm):
    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
            field.widget.attrs['class'] = 'login__input'


    # def __init__(self, *args, **kwargs):
    # super().__init__(*args, **kwargs)
    # self.fields['user_type'].widget = forms.RadioSelect(choices=CustomUser.USER_TYPE_CHOICES)
    # super(room_form, self).__init__(*args, **kwargs)
    # for field_name, field in self.fields.items():
    #     field.widget.attrs['placeholder'] = field.label
    #     field.widget.attrs['class'] = 'login__input'
