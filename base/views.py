from django.shortcuts import render ,redirect
from .form import resigration_Form ,Customer_form
from django.contrib.auth import login ,authenticate,logout
from django.contrib.auth.decorators import login_required
from  django.contrib import messages
from django.contrib.auth.models import User
from product.models import Product,Customer,ProductImage
from django.http import HttpResponseNotFound
from django import template 

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)


@login_required(login_url='login-page')
def admin_profile(request):
    if request.user.is_authenticated and request.user.is_staff:
        user=request.user
        return render(request, 'admin/admin_profile.html')
    else:
        return redirect('login-page')
@login_required(login_url='login-page')
def user_profile(request,id):
    user = User.objects.get(id=id)
    
    try:
        customer = Customer.objects.get(user__username=user.username)
        products=Product.objects.filter(posted_by=user)
        productimage = {}
        for product in products:
            if image := ProductImage.objects.filter(product=product).first():
                productimage[product.id] = image.image
    except Customer.DoesNotExist:
        return HttpResponseNotFound("Customer profile not found.")
    return render(request, 'customer/customer_profiles.html', {'productimage': productimage,
                                    'products':products,'customer': customer})
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
        login(request, user)  
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

def update_customeze_register_page(request,user_id):  
    user=User.objects.get(id=user_id) 
    if request.method == "POST": 
        user_form = resigration_Form(request.POST,instance=user)
        if user_form.is_valid(): 
            return update_customeze_register_page(user_form, request) 
    else: 
        user_form = resigration_Form(instance=user) 
    context= {
        'user_form': user_form}
    return render(request, 'base/register_page.html',context)

def update_extracted_from_register_page_6(user_form, request):
    user = user_form.save() 
    return redirect('customer-details')



def update_customer_details(request,c_id):
    customer=Customer.objects.get(id=c_id)
    form=Customer_form(instance=customer)
    if request.method == "POST":
        form=Customer_form(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer-details')
        else:
            messages.error(request,"error please enter valid info")
    return render(request, 'base/create_customer.html',{"form":form})
def delete_customer_details(request,c_id):
    customer=Customer.objects.get(id=c_id)
    customer.blocked=True
    customer.save()
    return redirect('customer-details')
    