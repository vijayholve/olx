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
class PaymentType(models.Model):
    name=models.CharField(max_length=100)
class Transaction(models.Model):
    Customer=models.ForeignKey(User,on_delete=models.CASCADE, 
                               related_name="transactions")
    amount=models.IntegerField()
    plan=models.ForeignKey(Plan, on_delete=models.CASCADE)
    payment_type=models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
import uuid
from django.db import models
from django.contrib.auth.models import User  # Assuming you have a User model

class Order(models.Model):
    order_no = models.AutoField(primary_key=True)  # Automatically increments
    transaction_no = models.CharField(max_length=36, unique=True, blank=True)  # UUID as a unique transaction number
    plan_name = models.CharField(max_length=255)  # Name of the plan
    payment_type = models.CharField(max_length=50)  # e.g., Credit Card, PayPal, etc.
    customer = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference to the User who made the order
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount in dollars
    created_time = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp when created
    payment_status = models.CharField(max_length=50)  # e.g., Paid, Pending, Failed

    def save(self, *args, **kwargs):
        if not self.transaction_no:
            # Generate a unique transaction number using UUID
            self.transaction_no = str(uuid.uuid4())  # Convert UUID to string
        super().save(*args, **kwargs)  # Call the original save method

    def __str__(self):
        return f"Order {self.order_no} - {self.plan_name} by {self.customer.username}"
	

