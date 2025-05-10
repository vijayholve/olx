import os
import random
from faker import Faker
from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from product.models import (
    Customer, Product, ProductImage, State, Category,
    Features, Plan, PlanFeature, PaymentType
)

fake = Faker()

class Command(BaseCommand):
    help = "Generate fake data for testing"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating fake data...")

        # Create States and Categories if not exists
        if State.objects.count() == 0:
            for _ in range(5):
                State.objects.create(name=fake.state())

        if Category.objects.count() == 0:
            for _ in range(5):
                Category.objects.create(name=fake.word().capitalize())

        # Create Users and Customers
        for _ in range(10):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password="password"
            )
            Customer.objects.create(
                name=fake.name(),
                user=user,
                phone_no=fake.phone_number()[:15],
                email=user.email,
                address=fake.address(),
                profile_picture=None,
                verified_type=random.choice(['verified', 'unverified', 'most viewed'])
            )

        # Fetch data
        states = list(State.objects.all())
        categories = list(Category.objects.all())
        users = list(User.objects.all())

        image_dir = os.path.join(settings.MEDIA_ROOT)
        available_images = [
            os.path.join(image_dir, img)
            for img in os.listdir(image_dir)
            if img.lower().endswith(('.jpg', '.jpeg', '.png'))
        ]

        if not available_images:
            self.stdout.write(self.style.ERROR("No images found in media/product_images/. Please add some first."))
            return

        # Create Products with ProductImages
        for _ in range(20):
            product = Product.objects.create(
                title=fake.word().capitalize(),
                description=fake.paragraph(),
                price=round(random.uniform(10, 1000), 2),
                category=random.choice(categories),
                location=fake.city(),
                condition=random.choice(['New', 'Used']),
                posted_by=random.choice(users),
                state=random.choice(states),
                is_active=True,
            )

            for _ in range(random.randint(1, 4)):
                image_path = random.choice(available_images)
                with open(image_path, 'rb') as img_file:
                    ProductImage.objects.create(
                        product=product,
                        image=File(img_file, name=os.path.basename(image_path))
                    )

        # Create Plans and Features
        features = Features.objects.all()
        plans = []
        for _ in range(5):
            plan = Plan.objects.create(
                name=fake.word().capitalize(),
                plan_type=random.choice(['one time', 'recurring']),
                price=random.randint(50, 500)
            )
            plans.append(plan)

        for plan in plans:
            for feature in features:
                PlanFeature.objects.create(
                    plan=plan,
                    feature=feature,
                    included=random.choice([True, False])
                )

        self.stdout.write(self.style.SUCCESS("Successfully created fake data with images!"))
