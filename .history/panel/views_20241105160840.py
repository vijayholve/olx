from django.shortcuts import render
from product.models import Product,ProductImage,User

def admin_panel(request):
    if request.user.is_authenticated and request.user.is_staff:
        products = Product.objects.all()
        images = ProductImage.objects.all()
        users = User.objects.all()
        
        context = {
            'products': products,
            'images': images,
            'users': users,
        }
        return render(request, 'admin/admin_panel.html', context)