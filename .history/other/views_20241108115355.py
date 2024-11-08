from django.shortcuts import render,redirect
from .form import StateForm, CategoryForm, FeaturesForm, PaymentTypeForm, TransactionForm, OrderForm
from django.contrib.auth.decorators import login_required
from product.models import Product,class Inline(admin.StackedInline):
    '''Stacked Inline View for '''

    model = 
    min_num = 3
    max_num = 20
    extra = 1
    raw_id_fields = (,)
@login_required(login_url="login-page")
def state_details(request):
    operation="view"
    title="States"
    states = State.objects.all()
    return render(request, 'state_details.html', {'states': states,
                                                 "operation": operation,
                                                 "title": title}
                  )

@login_required(login_url="login-page")
def create_state(request):
    operation="create"
    title="State"
    if request.method == 'POST':
        form = StateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some_view_name')
    else:
        form = StateForm()
    return render(request, 'create_state.html', {'form': form,
                                                 "operation": operation,
                                                 "title": title}
                  )

# Create your views here.
