from django.contrib import admin

from .models import Product,ProductImage,Transaction,Order
list_models=[
    Product,
    # Status,
    ProductImage
]
for model in list_models:
    admin.site.register(model)
