from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from inventory.models import Inventory, Supplier
from faker import Faker
import random

fake = Faker()
product_categories = ["Laptop", "Phone", "Keyboard", "Monitor", "Printer", "Desk", "Chair", "Tablet", "Mouse", "Speaker"]

class Command(BaseCommand):
    help = "Seeds the database with sample inventory data"

    def handle(self, *args, **kwargs):
        for _ in range(5):
            supplier = Supplier.objects.create(name=fake.company())

        for _ in range(15):
            Inventory.objects.create(
                name=f"{fake.color_name()} {random.choice(product_categories)}",
                description=fake.sentence(),
                note=fake.text(),
                stock=fake.random_int(min=1, max=100),
                availability=True,
                supplier=Supplier.objects.order_by("?").first()
            )

        for _ in range(5):
            Inventory.objects.create(
                name=f"{fake.color_name()} {random.choice(product_categories)}",
                description=fake.sentence(),
                note=fake.text(),
                stock=0,
                availability=False,
                supplier=Supplier.objects.order_by("?").first()
            )

        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "admin123")
            self.stdout.write(self.style.SUCCESS("Superuser 'admin' created successfully!"))


        self.stdout.write(self.style.SUCCESS("Successfully seeded the database!"))
