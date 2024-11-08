from django.shortcuts import render,redirect
from .form import StateForm, CategoryForm, FeaturesForm, PaymentTypeForm, TransactionForm, OrderForm
from django.contrib.auth.decorators import login_required
from product.models import Product,State,Category ,Transaction,Order,PaymentType,Features
@login_required(login_url="login-page")
def state_details(request):
    category= Category.objects.filter(blocked=False)
    states = State.objects.filter(blocked=False)
    content={'states': states,"category":category}
    return render(request, 'other/details_state.html', content)

@login_required(login_url="login-page")
def create_state(request):
    if request.method == 'POST':
        form = StateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details_state')
    else:
        form = StateForm()
    return render(request, 'other/create_state.html', {'form': form})

@login_required(login_url="login-page")
def update_state(request,pk):
    state=State.objects.get(id=pk)
    if request.method == 'POST':
        form = StateForm(request.POST, instance=state)
        if form.is_valid():
            form.save()
            return redirect('details_state')
    else:
        form = StateForm( instance=state)
    return render(request, 'other/update_state.html', {'form': form})

@login_required(login_url="login-page")
def delete_state(request,pk):
    state=State.objects.get(id=pk)
    state.block()
    return redirect('details_state')
@login_required(login_url="login-page")
def category_details(request):
    category= Category.objects.filter(blocked=False)
    return render(request, 'other/details_category.html', {'category': category})

@login_required(login_url="login-page")
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details_category')
    else:
        form = CategoryForm()
    return render(request, 'other/create_category.html', {'form': form})

@login_required(login_url="login-page")
def update_category(request,pk):
    category=Category.objects.get(id=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('details_category')
    else:
        form = CategoryForm( instance=category)
    return render(request, 'other/update_category.html', {"form":form,'category': category})

@login_required(login_url="login-page")
def delete_category(request,pk):
    category=Category.objects.get(id=pk)
    category.block()
    return redirect('details_category')


ransaction
@login_required(login_url="login-page")
def category_details(request):
    category= Category.objects.filter(blocked=False)
    return render(request, 'other/details_category.html', {'category': category})

@login_required(login_url="login-page")
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details_category')
    else:
        form = CategoryForm()
    return render(request, 'other/create_category.html', {'form': form})

@login_required(login_url="login-page")
def update_category(request,pk):
    category=Category.objects.get(id=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('details_category')
    else:
        form = CategoryForm( instance=category)
    return render(request, 'other/update_category.html', {"form":form,'category': category})

@login_required(login_url="login-page")
def delete_category(request,pk):
    category=Category.objects.get(id=pk)
    category.block()
    return redirect('details_category')
