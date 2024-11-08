from django.shortcuts import render,redirect
from product.models import Product, ProductImage, User, State, Plan, Transaction, Order, Customer,Category
from django.db.models import Count, Sum
from datetime import datetime
import json
from django.contrib.auth.decorators import login_required
from product.forms import ProductForm,MultipleImagesForm
from  django.contrib import messages

@login_required(login_url='login-page')
def admin_panel(request):
    if request.user.is_authenticated and request.user.is_staff:
        products = Product.objects.filter(blocked=False)
        images = ProductImage.objects.filter(blocked=False)
        users = User.objects.filter(is_active=True)  
        states_with_product_count = (
            State.objects.filter(blocked=False)
            .annotate(product_count=Count('product'))
            .values('name', 'product_count')
        )

        all_states = []
        all_states_product_count = []

        for state in states_with_product_count:
            all_states.append(state['name'])
            all_states_product_count.append(state['product_count'])
        
        context = {
            'all_states': all_states,
            'all_states_product_count': all_states_product_count,
            'products': products,
            'images': images,
            'users': users,
        }
        return render(request, 'panel/admin_panel.html', context)
@login_required(login_url='login-page')
def plan_list(request):
    plans = Plan.objects.prefetch_related('planfeature_set__feature').filter(blocked=False).order_by('-id')
    return render(request, 'panel/plan_details.html', {'plans': plans})
@login_required(login_url='login-page')
def plan_delete():
    pass
@login_required(login_url='login-page')
def sales_report(request):
    transactions = Transaction.objects.filter(blocked=False)
    orders = Order.objects.filter(blocked=False)

    # Aggregate sales data by month
    monthly_sales = (
        Order.objects
        .filter(blocked=False)
        .extra(select={'month': "EXTRACT(month FROM created_time)"})
        .values('month')
        .annotate(total_amount=Sum('amount'))
        .order_by('month')
    )

    monthly_data = {month: 0 for month in range(1, 13)}  # Dictionary with all months initialized to zero
    for entry in monthly_sales:
        monthly_data[int(entry['month'])] = float(entry['total_amount'])  # Fill with actual data

    # Prepare data for Chart.js
    labels = [datetime(2000, month, 1).strftime('%B') for month in range(1, 13)]  # Full month names
    data = [monthly_data[month] for month in range(1, 13)]  # Monthly totals with zero-filled months

    chart_data = {
        'labels': labels,
        'datasets': [
            {
                'label': 'Total Sales',
                'data': data,
                'backgroundColor': 'rgba(75, 192, 192, 0.2)',
                'borderColor': 'rgba(75, 192, 192, 1)',
                'borderWidth': 1,
            }
        ]
    }

    products = Product.objects.filter(blocked=False)
    images = ProductImage.objects.filter(blocked=False)
    users = User.objects.filter(is_active=True)  # Assuming inactive users are blocked
    states_with_product_count = (
        State.objects.filter(blocked=False)
        .annotate(product_count=Count('product'))
        .values('name', 'product_count')
    )
    
    # Prepare the labels and data lists
    all_states = []
    all_states_product_count = []

    for state in states_with_product_count:
        all_states.append(state['name'])
        all_states_product_count.append(state['product_count'])
    
    total_orders = orders.count()
    total_customers = Customer.objects.filter(blocked=False).count()
    total_plan = Plan.objects.filter(blocked=False).count()
    total_products = products.count()
    customers = Customer.objects.filter(blocked=False)
    total_state = State.objects.filter(blocked=False).count()
    total_sold_products = Product.objects.filter(is_active=True, blocked=False).count()

    context = {
        'all_states': all_states,
        'all_states_product_count': all_states_product_count,
        'products': products,
        'images': images,
        'users': users,
        'transactions': transactions,
        'orders': orders,
        'chart_data': json.dumps(chart_data),
        "total_orders": total_orders,
        "total_customers": total_customers,
        "total_plan": total_plan,
        "total_products": total_products,
        "total_state": total_state,
        "total_sold_products": total_sold_products,
        "customers": customers
    }
    return render(request, 'panel/home_panel.html', context)
@login_required(login_url='login-page')
def customer_details(request):
    customers = Customer.objects.filter(blocked=False)
    return render(request, 'panel/customer_detail.html', {'customers': customers})

def product_all_detail(request):
    products = Product.objects.filter(blocked=False)
    return render(request, 'panel/product_detail.html', {'products': products})
def product_categreriry_detail(request,catg_id):
    category=Category.objects.get(id=catg_id)
    products = Product.objects.filter(blocked=False, category=category)
    return render(request, 'panel/product_detail.html', {'products': products})