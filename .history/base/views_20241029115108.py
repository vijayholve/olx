from django.shortcuts import render
from forms import 
# Create your views here.
def customeze_register_page(request): 
    ser_form = CustomUserCreationForm()
    if request.method == "POST": 
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid(): 
            return _extracted_from_register_page_6(user_form, request)
    else: 
        user_form = CustomUserCreationForm() 
    context= {
        'user_form': user_form,
     
    }
    return render(request, 'base/register.html',context)