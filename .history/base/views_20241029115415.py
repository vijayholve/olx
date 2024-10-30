from django.shortcuts import render ,redirect
from forms import resigration_Form 
from django.contrib.auth import login ,authenticate,logout,red

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

            
            
def _extracted_from_register_page_6(user_form, request):
    user = user_form.save()
    user_type = request.POST.get('user_type') 
    print("user type is",user_type)
    authenticate( user)
    login(request,user)
    return redirect('user-type',user_id=user.id ,user_type=user_type)  