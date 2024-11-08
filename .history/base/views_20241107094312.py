from django.shortcuts import render ,redirect
from .form import resigration_Form 
from django.contrib.auth import login ,authenticate,logout
from django.contrib.auth.decorators import login_required
from  django.contrib import messages

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
    return render(request, 'base/register_page.html',context)

def _extracted_from_register_page_6(user_form, request):
    user = user_form.save()  # Saves the user to the database
    user = authenticate(username=user.username, password=user.password)  # Authenticate the user
    if user is not None:
        login(request, user)  # Log the user in
    return redirect('home')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if user := authenticate(username=username, password=password):
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login-page')  # Redirect to refresh the page with error message


    return render(request, 'base/login_page.html')

@login_required(login_url='login-page')
def logout_page(request):
    logout(request)
    return redirect('login-page')

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
    return render(request, 'base/register_page.html',context)

def _extracted_from_register_page_6(user_form, request):
    user = user_form.save()  # Saves the user to the database
    user = authenticate(username=user.username, password=user.password)  # Authenticate the user
    if user is not None:
        login(request, user)  # Log the user in
    return redirect('home')