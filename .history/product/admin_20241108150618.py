from django.contrib import admin

from .models import Product,ProductImage,Order ,Customer, State,Category,Product,ProductImage,Features,Plan,PaymentType
list_models=[
Order ,Customer, State,Category,Product,ProductImage,Features,Plan,PaymentType
]
for model in list_models:
    admin.site.register(model)
