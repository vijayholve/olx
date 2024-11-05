from django.contrib import admin

from .models import Product,ProductImage,Transaction,Order,Status
list_models=[
    Product,
    s,
    ProductImage
]
for model in list_models:
    admin.site.register(model)
