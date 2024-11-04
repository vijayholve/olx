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
    authenticate( user)
    login(request,user)
    return redirect('home') 

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
    return render(request, 'base/login.html')