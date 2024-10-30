from django.contrib import admin

from .models import Product,ProductImage

list_models=[
    Product,
    ProductImage
]
admin.site.register(Product)
