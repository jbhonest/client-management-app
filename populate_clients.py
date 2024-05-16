from faker import Faker
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clients_project.settings')
django.setup()

from clients_app.models import Client
fake = Faker()

# Generate fake data and save to the database


def generate_fake_clients(n):
    for _ in range(n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        Client.objects.create(first_name=first_name,
                              last_name=last_name, email=email)


# Call the function to generate 10 fake clients
generate_fake_clients(10)
