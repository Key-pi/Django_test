from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand

from faker import Faker

UserModel = get_user_model()


class Command(BaseCommand):
    help = "Create random users" # noqa A003

    def add_arguments(self, parser):
        parser.add_argument("total", type=int, choices=range(1, 11), help='Number of users to create')

    def handle(self, *args, **options):
        fake = Faker()
        total = options['total']
        obj = [
            UserModel(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                username=fake.name(),
                email=fake.email(),
                password=make_password('Password_easy')
            )
            for _ in range(total)
        ]

        UserModel.objects.bulk_create(obj)
        print("Users Created!") # noqa T001
