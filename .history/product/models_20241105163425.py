from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    name=models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    phone_no = models.CharField(max_length=12)
    email= models.EmailField(max_length=100)
    address = models.CharField(max_length=255)
    about_me = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    def __str__(self):
        return self.name
class State(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    CONDITION_CHOICES = [
        ('New', 'New'),
        ('Used', 'Used'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    location = models.CharField(max_length=255)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    date_posted = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  #activation/deactivation
    state=models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.title 
    
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='product_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.product.title}"
class Plan( models.Model):
    name=models.CharField(max_length=100)
class Transaction(models.Model):
    Customer=models.ForeignKey(User,on_delete=models.CASCADE, 
                               related_name="transactions")
    Amount=models.IntegerField()
    plan=models.ForeignKey(Plan, on_delete=models.CASCADE)
    payment_type=	