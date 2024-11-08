import random
import uuid
from faker import Faker
from django.core.management.base import BaseCommand
from product.models import User, Transaction, Order, Plan, PaymentType

fake = Faker()

class Command(BaseCommand):
    help = 'Generate fake data for Transaction and Order models'

    def handle(self, *args, **kwargs):
        # Create fake Transactions
        users = list(User.objects.all())
        plans = list(Plan.objects.all())
        payment_types = list(PaymentType.objects.all())

        if not users or not plans or not payment_types:
            self.stdout.write("Ensure you have User, Plan, and PaymentType records in the database.")
            return

        # Generate fake transactions
        for _ in range(50):  # Adjust the number of fake records as needed
            transaction = Transaction.objects.create(
                customer=random.choice(users),
                transaction_no=str(uuid.uuid4()),
                amount=random.randint(100, 10000),
                plan=random.choice(plans),
                payment_type=random.choice(payment_types)
            )
            self.stdout.write(f"Created Transaction {transaction.transaction_no}")

        # Generate fake orders based on existing transactions
        transactions = list(Transaction.objects.all())
        for _ in range(50):  # Adjust the number of fake records as needed
            order = Order.objects.create(
                transaction=random.choice(transactions),
                plan=random.choice(plans),
                payment_type=random.choice(payment_types),
                customer=random.choice(users),
                amount=fake.pydecimal(left_digits=4, right_digits=2, positive=True),
                payment_status=fake.boolean()
            )
            self.stdout.write(f"Created Order {order.order_no}")

        self.stdout.write(self.style.SUCCESS('Successfully generated fake data!'))
