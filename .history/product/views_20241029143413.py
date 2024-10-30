from django.shortcuts import render,redirect
from .forms import ProductForm,MultipleImagesForm,ProductImage
from .models import Product ,ProductImage,State
def home(request):
    return render(request,"product/home.html")
def product_create_form(request):
    number_of_image_fields = 4
    product_form = ProductForm(request.POST or None)  # Keep the form state in case of invalid submission
    image_form = MultipleImagesForm(request.FILES or None)
    if request.method == 'POST':
        print(product_form.errors)  # Log product form errors
        print(image_form.errors)   
        if product_form.is_valid() and image_form.is_valid():
            product = product_form.save(commit=False)
            product.posted_by = request.user
            product.save()

            # Handle the images
            images = request.FILES.getlist('images')
            for img in images:
                ProductImage.objects.create(product=product, image=img)

            return redirect('home')
    
    # The forms are already created, no need for else block
    context = {
        'number_of_image_fields': range(number_of_image_fields),  # Pass the range as context
        'product_form': product_form,
        'image_form': image_form,
    }

    return render(request, 'product/create_product.html', context)

