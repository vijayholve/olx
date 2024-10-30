from django.contrib import admin

from .models import Product,ProductImage

list_models=[
    Product,
    ProductImage
]
for lis
admin.site.register(Product)
