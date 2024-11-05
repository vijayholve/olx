from django.contrib import admin

from .models import Product,ProductImage,te

list_models=[
    Product,
    ProductImage
]
for model in list_models:
    admin.site.register(model)
