from django.shortcuts import render,redirect
from .forms import ProductForm,MultipleImagesForm,ProductImage
from .models import Product ,ProductImage,State
def home(request):
    return render(request,"product/home.html")
def product_create_form(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        image_form = MultipleImagesForm(request.FILES)

        if product_form.is_valid() and image_form.is_valid():
            product = product_form.save(commit=False)
            product.posted_by = request.user
            product.save()

            # Handle the images
            images = request.FILES.getlist('images')
            if len(images) < 20:
                image_form.add_error('images', 'You must upload at least 20 images.')
            else:
                for img in images:
                    ProductImage.objects.create(product=product, image=img)

                return redirect('product_detail', pk=product.pk)

    else:
        product_form = ProductForm()
        image_form = MultipleImagesForm()
        number_of_image_fields = 4  # You can set this to any number you want

    context = {
        'product_form': product_form,
        'image_form': image_form,
        'number_of_image_fields': range(number_of_image_fields),  # Pass the range as context
        'product_form': product_form,
        'image_form': image_form,
    }

    return render(request, 'product/create_product.html', context)
