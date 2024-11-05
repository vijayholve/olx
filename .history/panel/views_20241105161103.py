from django.shortcuts import render
from product.models import Product,ProductImage,User

def admin_panel(request):
    if request.user.is_authenticated and request.user.is_staff:
        products = Product.objects.all()
        images = ProductImage.objects.all()
        users = User.objects.all()
        states_with_product_count = State.objects.annotate(product_count=Count('product')).values('name', 'product_count')
        context = {
            'products': products,
            'images': images,
            'users': users,
        }
        return render(request, 'admin/admin_panel.html', context)