from django.shortcuts import render
from product.models import Product,ProductImage,User,State,Plan
from django.db.models import Count

def admin_panel(request):
    if request.user.is_authenticated and request.user.is_staff:
        products = Product.objects.all()
        images = ProductImage.objects.all()
        users = User.objects.all()
        states_with_product_count = State.objects.annotate(product_count=Count('product')).values('name', 'product_count')

    # Prepare the labels and data lists
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
        return render(request, 'admin/admin_panel.html', context)


from django.shortcuts import render
from .models import Plan

def plan_list(request):
    plans = Plan.objects.prefetch_related('planfeature_set__feature').all()
    return render(request, 'your_template.html', {'plans': plans})
