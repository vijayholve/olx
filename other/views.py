from django.shortcuts import render, redirect
from .form import StateForm, CategoryForm, FeaturesForm, PaymentTypeForm, OrderForm
from django.contrib.auth.decorators import login_required
from product.models import Product, State, Category, Order, PaymentType, Features

@login_required(login_url="login-page")
def state_details(request):
    category = Category.objects.filter(blocked=False)  # Added line
    states = State.objects.filter(blocked=False)
    content = {'states': states, "category": category}
    return render(request, 'other/details_state.html', content)

@login_required(login_url="login-page")
def create_state(request):
    category = Category.objects.filter(blocked=False)  # Added line
    if request.method == 'POST':
        form = StateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details_state')
    else:
        form = StateForm()
    return render(request, 'other/create_state.html', {'form': form, 'category': category})

@login_required(login_url="login-page")
def update_state(request, pk):
    category = Category.objects.filter(blocked=False)  # Added line
    state = State.objects.get(id=pk)
    if request.method == 'POST':
        form = StateForm(request.POST, instance=state)
        if form.is_valid():
            form.save()
            return redirect('details_state')
    else:
        form = StateForm(instance=state)
    return render(request, 'other/update_state.html', {'form': form, 'category': category})

@login_required(login_url="login-page")
def delete_state(request, pk):
    category = Category.objects.filter(blocked=False)  # Added line
    state = State.objects.get(id=pk)
    state.block()
    return redirect('details_state')

@login_required(login_url="login-page")
def category_details(request):
    category = Category.objects.filter(blocked=False)  # Added line
    return render(request, 'other/details_category.html', {'category': category})

@login_required(login_url="login-page")
def create_category(request):
    category = Category.objects.filter(blocked=False)  # Added line
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details_category')
    else:
        form = CategoryForm()
    return render(request, 'other/create_category.html', {'form': form, 'category': category})

@login_required(login_url="login-page")
def update_category(request, pk):
    category = Category.objects.filter(blocked=False)  # Added line
    category_obj = Category.objects.get(id=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category_obj)
        if form.is_valid():
            form.save()
            return redirect('details_category')
    else:
        form = CategoryForm(instance=category_obj)
    return render(request, 'other/update_category.html', {"form": form, 'category': category, 'category_obj': category_obj})

@login_required(login_url="login-page")
def delete_category(request, pk):
    category = Category.objects.filter(blocked=False)  # Added line
    category_obj = Category.objects.get(id=pk)
    category_obj.block()
    return redirect('details_category')

@login_required(login_url="login-page")
def order_details(request):
    category = Category.objects.filter(blocked=False)  # Added line
    orders = Order.objects.filter(blocked=False)
    context = {'orders': orders, "category": category}
    return render(request, 'other/details_order.html', context)

@login_required(login_url="login-page")
def create_order(request):
    category = Category.objects.filter(blocked=False)  # Added line
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details_order')
    else:
        form = OrderForm()
    return render(request, 'other/create_order.html', {'form': form, 'category': category})

@login_required(login_url="login-page")
def update_order(request, pk):
    category = Category.objects.filter(blocked=False)  # Added line
    order = Order.objects.get(order_no=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('details_order')
    else:
        form = OrderForm(instance=order)
    return render(request, 'other/update_order.html', {'form': form, 'category': category})

@login_required(login_url="login-page")
def delete_order(request, pk):
    category = Category.objects.filter(blocked=False)  # Added line
    order = Order.objects.get(order_no=pk)
    order.block()
    return redirect('details_order')

@login_required(login_url="login-page")
def paymentType_details(request):
    category = Category.objects.filter(blocked=False)  # Added line
    paymentTypes = PaymentType.objects.filter(blocked=False)
    context = {'paymentTypes': paymentTypes, "category": category}
    return render(request, 'other/details_paymentType.html', context)

@login_required(login_url="login-page")
def create_paymentType(request):
    category = Category.objects.filter(blocked=False)  # Added line
    if request.method == 'POST':
        form = PaymentTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details_paymentType')
    else:
        form = PaymentTypeForm()
    return render(request, 'other/create_paymentType.html', {'form': form, 'category': category})

@login_required(login_url="login-page")
def update_paymentType(request, pk):
    category = Category.objects.filter(blocked=False)  # Added line
    paymentType = PaymentType.objects.get(id=pk)
    if request.method == 'POST':
        form = PaymentTypeForm(request.POST, instance=paymentType)
        if form.is_valid():
            form.save()
            return redirect('details_paymentType')
    else:
        form = PaymentTypeForm(instance=paymentType)
    return render(request, 'other/update_paymentType.html', {'form': form, 'category': category})

@login_required(login_url="login-page")
def delete_paymentType(request, pk):
    category = Category.objects.filter(blocked=False)  # Added line
    paymentType = PaymentType.objects.get(id=pk)
    paymentType.block()
    return redirect('details_paymentType')

@login_required(login_url="login-page")
def feature_details(request):
    category = Category.objects.filter(blocked=False)  # Added line
    features = Features.objects.filter(blocked=False)
    context = {'features': features, "category": category}
    return render(request, 'other/details_feature.html', context)

@login_required(login_url="login-page")
def create_feature(request):
    category = Category.objects.filter(blocked=False)  # Added line
    if request.method == 'POST':
        form = FeaturesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details_feature')
    else:
        form = FeaturesForm()
    return render(request, 'other/create_feature.html', {'form': form, 'category': category})

@login_required(login_url="login-page")
def update_feature(request, pk):
    category = Category.objects.filter(blocked=False)  # Added line
    feature = Features.objects.get(id=pk)
    if request.method == 'POST':
        form = FeaturesForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('details_feature')
    else:
        form = FeaturesForm(instance=feature)
    return render(request, 'other/update_features.html', {'form': form, 'category': category})

@login_required(login_url="login-page")
def delete_feature(request, pk):
    category = Category.objects.filter(blocked=False)  # Added line
    feature = Features.objects.get(id=pk)
    feature.block()
    return redirect('details_feature')
