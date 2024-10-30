from django.shortcuts import render,redirect
from .forms import ProductForm,MultipleImagesForm,ProductImage
from .models import Product ,ProductImage,State
def home(request):
    products=Product.objects.all()
    for product in products:
        images = ProductImage.objects.filter(product=product).first()
        productimage{}
    context = {
        'products': products,
    }
    return render(request,"product/home.html",context)
def product_create_form(request):
    number_of_image_fields = 4
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        image_form = MultipleImagesForm(request.FILES)
        print(product_form)
        print(image_form)

        if product_form.is_valid() or image_form.is_valid():
            product = product_form.save(commit=False)
            product.posted_by = request.user
            product.save()

            # Handle the images
            images = request.FILES.getlist('images')
            
            for img in images:
                ProductImage.objects.create(product=product, image=img)

            return redirect('home')
    else:
        product_form = ProductForm()
        image_form = MultipleImagesForm()

    context = {
        'number_of_image_fields': range(number_of_image_fields),  # Pass the range as context
        'product_form': product_form,
        'image_form': image_form,
    }

    return render(request, 'product/create_product.html', context)


