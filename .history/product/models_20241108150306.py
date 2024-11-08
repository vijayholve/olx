from django.db import models
from django.contrib.auth.models import User
import uuid

#here is we add blocked insted of delete tables we just blocked
class Customer(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    phone_no = models.CharField(max_length=15) 
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    verified_type = models.CharField(max_length=100, choices=(
        ('verified', 'verified'),
        ('unverified', 'unverified'),
        ('most viewed', 'most viewed'),
    ))
    blocked = models.BooleanField(default=False)

    def block(self):
        self.blocked = True
        self.save()

    def unblock(self):
        self.blocked = False
        self.save()

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=100)
    blocked = models.BooleanField(default=False)

    def block(self):
        self.blocked = True 
        self.save()

    def unblock(self):
        self.blocked = False
        self.save()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    blocked = models.BooleanField(default=False)

    def block(self):
        self.blocked = True
        self.save()

    def unblock(self):
        self.blocked = False
        self.save()

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100)
    blocked = models.BooleanField(default=False)

    def block(self):
        self.blocked = True
        self.save()

    def unblock(self):
        self.blocked = False
        self.save()


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
    is_active = models.BooleanField(default=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    blocked = models.BooleanField(default=False)

    def block(self):
        self.blocked = True
        self.save()

    def unblock(self):
        self.blocked = False
        self.save()

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='product_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    blocked = models.BooleanField(default=False)

    def block(self):
        self.blocked = True
        self.save()

    def unblock(self):
        self.blocked = False
        self.save()

    def __str__(self):
        return f"Image for {self.product.title}"


class Features(models.Model):
    name = models.CharField(max_length=100) 
    blocked = models.BooleanField(default=False) 

    def block(self):
        self.blocked = True
        self.save()

    def unblock(self):
        self.blocked = False
        self.save()

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=100)
    CONDITION_CHOICES = [
        ('one time', 'One Time'),
        ('recurring', 'Recurring'),
    ]
    plan_type = models.CharField(max_length=10, choices=CONDITION_CHOICES, null=True, blank=True)
    price = models.IntegerField()
    blocked = models.BooleanField(default=False)

    def block(self):
        self.blocked = True
        self.save()

    def unblock(self):
        self.blocked = False
        self.save()

    def __str__(self):
        return self.name


class PlanFeature(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    feature = models.ForeignKey(Features, on_delete=models.CASCADE)
    included = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)

    def block(self):
        self.blocked = True
        self.save()

    def unblock(self):
        self.blocked = False
        self.save()

    def __str__(self):
        return f"{self.plan.name} - {self.feature.name}"


class PaymentType(models.Model):
    name = models.CharField(max_length=100)
    blocked = models.BooleanField(default=False)

    def block(self):
        self.blocked = True
        self.save()

    def unblock(self):
        self.blocked = False
        self.save()


class Transaction(models.Model):
    Customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    transaction_no = models.CharField(max_length=36, unique=True, blank=True)
    amount = models.IntegerField()
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    blocked = models.BooleanField(default=False)

    def block(self):
        self.blocked = True
        self.save()

    def unblock(self):
        self.blocked = False
        self.save()

    def save(self, *args, **kwargs):
        if not self.transaction_no:
            self.transaction_no = str(uuid.uuid4())  
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Transaction {self.transaction_no}"


class Order(models.Model):
    order_no = models.AutoField(primary_key=True)
    transaction_no = models.CharField(max_length=36, unique=True, blank=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_time = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField()  # False for unpaid/pending, True for paid
    blocked = models.BooleanField(default=False)

    def block(self):
        self.blocked = True
        self.save()

    def unblock(self):
        self.blocked = False
        self.save()
    

    def mark_as_paid(self):
        """Mark the order as paid and create a transaction."""
        if not self.payment_status:  # Check if it's not already marked as paid
            self.payment_status = True
            self.save()

            # Create a transaction
            transaction = Transaction.objects.create(
                customer=self.customer,
                transaction_no=str(uuid.uuid4()),
                amount=self.amount,
                plan=self.plan,
                payment_type=self.payment_type
            )
            return transaction

    def __str__(self):
        return f"Order {self.order_no} - {self.plan} by {self.customer.username}"
