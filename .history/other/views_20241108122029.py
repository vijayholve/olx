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
    if request.method == 'POST':
        state.delete()
        return redirect('details_state')
    return render(request, 'other/delete_state.html', {'state': state})