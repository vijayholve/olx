import random
import uuid
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from product.models import Customer, Product, ProductImage, State, Category, Status, Features, Plan, PaymentType, Transaction, Order

fake = Faker()

class Command(BaseCommand):
    help = "Generate fake data for testing"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating fake data...")
        for _ in range(50):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password="password"
            )
            Customer.objects.create(
                name=fake.name(),
                user=user,
                phone_no=fake.phone_number()[:15] ,
                email=user.email,
                address=fake.address(),
                profile_picture=None,
                verified_type=random.choice(['verified', 'unverified', 'most viewed'])
            )

        # Step 3: Create Products
        states = State.objects.all()
        categories = Category.objects.all()
        for _ in range(100):
            product = Product.objects.create(
                title=fake.word(),
                description=fake.paragraph(),
                price=round(random.uniform(10, 1000), 2),
                category=random.choice(categories),
                location=fake.city(),
                condition=random.choice(['New', 'Used']),
                posted_by=random.choice(User.objects.all()),
                state=random.choice(states),
                is_active=True,
            )
            # Step 4: Add Images for each Product
            for _ in range(random.randint(1, 5)):
                ProductImage.objects.create(
                    product=product,
                    image=None  # Replace with actual image file if available
                )

        # Step 5: Create Plans
        features = Feature.objects.all()
    plans = []

    # Create Plans
    for _ in range(20):
        plan = Plan.objects.create(
            name=fake.word(),
            plan_type=random.choice(['one time', 'recurring']),
            price=random.randint(100, 1000)
        )
        plans.append(plan)

    # Assign Features to Plans
    for plan in plans:
        for feature in features:
            PlanFeature.objects.create(
                plan=plan,
                feature=feature,
                included=random.choice([True, False])  # Randomly mark as included or not
            )

        # Step 6: Create Transactions and Orders
        payment_types = PaymentType.objects.all()
        plans = Plan.objects.all()
        for _ in range(100):
            transaction = Transaction.objects.create(
                Customer=random.choice(User.objects.all()),
                amount=random.randint(10, 1000),
                plan=random.choice(plans),
                payment_type=random.choice(payment_types)
            )

            Order.objects.create(
                transaction_no=str(uuid.uuid4()),
                plan=transaction.plan,
                payment_type=transaction.payment_type,
                customer=transaction.Customer,
                amount=transaction.amount,
                payment_status=random.choice([True, False]),
            )

        self.stdout.write(self.style.SUCCESS("Successfully created fake data!"))
