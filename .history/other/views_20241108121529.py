from django.shortcuts import render,redirect
from .form import StateForm, CategoryForm, FeaturesForm, PaymentTypeForm, TransactionForm, OrderForm
from django.contrib.auth.decorators import login_required
from product.models import Product,State
@login_required(login_url="login-page")
def state_details(request):
    states = State.objects.filter(blocked=False)
    return render(request, 'other/details_state.html', {'states': states})

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
def create_state(request):
    if request.method == 'POST':
        form = StateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details_state')
    else:
        form = StateForm()
    return render(request, 'other/create_state.html', {'form': form})