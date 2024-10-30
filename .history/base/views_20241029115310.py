from django.shortcuts import render
from forms import resigration_Form
# Create your views here.
def customeze_register_page(request): 
    ser_form = resigration_Form()
    if request.method == "POST": 
        user_form = resigration_Form(request.POST)
        if user_form.is_valid(): 
            return _extracted_from_register_page_6(user_form, request)
    else: 
        user_form = resigration_Form() 
    context= {
        'user_form': user_form,
     
    }
    return render(request, 'base/register.html',context)

            
