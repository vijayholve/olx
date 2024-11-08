from django.core.management.base import BaseCommand
from product.models import Transaction, Order, Plan, PaymentType
from django.contrib.auth.models import User
from faker import Faker
import random
import uuid

fake = Faker()

class Command(BaseCommand):
    help = 'Generate fake data for transactions and orders'

    def handle(self, *args, **kwargs):
        # Assuming there are already some users, plans, and payment types in the database
        users = User.objects.all()
        plans = Plan.objects.all()
        payment_types = PaymentType.objects.all()

        if not users.exists() or not plans.exists() or not payment_types.exists():
            self.stdout.write(self.style.ERROR('Please ensure users, plans, and payment types exist in the database'))
            return

        for _ in range(10):  # Change the range for more or fewer records
            user = random.choice(users)
            plan = random.choice(plans)
            payment_type = random.choice(payment_types)
            amount = random.randint(100, 1000)

            # Create an order
            order = Order.objects.create(
                transaction_no=str(uuid.uuid4()),
                plan=plan,
                payment_type=payment_type,
                customer=user,
                amount=amount,
                payment_status=random.choice([True, False])
            )

            self.stdout.write(self.style.SUCCESS(f'Order {order.order_no} created for user {user.username}'))

            if order.payment_status:  # If the order is marked as paid, create a transaction
                transaction = Transaction.objects.create(
                    Customer=user,
                    transaction_no=str(uuid.uuid4()),
                    amount=amount,
                    plan=plan,
                    payment_type=payment_type
                )
                self.stdout.write(self.style.SUCCESS(f'Transaction {transaction.transaction_no} created for order {order.order_no}'))
