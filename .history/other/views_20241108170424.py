from django.shortcuts import render,redirect
from .form import StateForm, CategoryForm, FeaturesForm, PaymentTypeForm, OrderForm, OrderForm
from django.contrib.auth.decorators import login_required
from product.models import Product,State,Category ,Order,PaymentType,Features
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



@login_required(login_url="login-page")
def order_details(request):
    category= Category.objects.filter(blocked=False)
    orders = Order.objects.filter(blocked=False)
    context = {
        'orders': orders,
            "category":category}
    return render(request, 'other/details_order.html', context)

@login_required(login_url="login-page") 
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details_order')
    else:
        form = OrderForm()
    return render(request, 'other/create_order.html', {'form': form})

@login_required(login_url="login-page")
def update_order(request,pk):
    order=Order.objects.get(order_no=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('details_order')
    else:
        form = OrderForm( instance=order)
    return render(request, 'other/update_order.html', {'form': form})

@login_required(login_url="login-page")
def delete_order(request,pk):
    order=Order.objects.get(order_no=pk)
    order.block()
    return redirect('details_order')


@login_required(login_url="login-page")
def paymentType_details(request):
    category= Category.objects.filter(blocked=False)
    paymentTypes = PaymentType.objects.filter(blocked=False)
    context = {
        'paymentTypes': paymentTypes,
            "category":category}
    return render(request, 'other/details_paymentType.html', context)

@login_required(login_url="login-page") 
def create_paymentType(request):
    if request.method == 'POST':
        form = PaymentTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details_paymentType')
    else:
        form = PaymentTypeForm()
    return render(request, 'other/create_paymentType.html', {'form': form})

@login_required(login_url="login-page")
def update_paymentType(request,pk):
    paymentType=PaymentType.objects.get(id=pk)
    if request.method == 'POST':
        form = PaymentTypeForm(request.POST, instance=paymentType)
        if form.is_valid():
            form.save()
            return redirect('details_paymentType')
    else:
        form = PaymentTypeForm( instance=paymentType)
    return render(request, 'other/update_paymentType.html', {'form': form})

@login_required(login_url="login-page")
def delete_paymentType(request,pk):
    paymentType=PaymentType.objects.get(id=pk)
    paymentType.block()
    return redirect('details_paymentType')



@login_required(login_url="login-page")
def feature_details(request):
    category= Category.objects.filter(blocked=False)
    features = Features.objects.filter(blocked=False)
    context = {
        'features': features,
            "category":category}
    return render(request, 'other/details_feature.html', context)

@login_required(login_url="login-page") 
def create_feature(request):
    if request.method == 'POST':
        form = FeaturesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details_feature')
    else:
        form = FeaturesForm()
    return render(request, 'other/create_feature.html', {'form': form})

@login_required(login_url="login-page")
def update_feature(request,pk):
    feature=Features.objects.get(id=pk)
    if request.method == 'POST':
        form = FeaturesForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('details_feature')
    else:
        form = FeatureForm( instance=feature)
    return render(request, 'other/update_feature.html', {'form': form})

@login_required(login_url="login-page")
def delete_feature(request,pk):
    feature=Feature.objects.get(id=pk)
    feature.block()
    return redirect('details_feature')