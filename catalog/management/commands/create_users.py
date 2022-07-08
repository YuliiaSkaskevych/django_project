from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Create faker users to DB'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, choices=range(1, 11), help='Number of the creating users')

    def handle(self, *args, **options):
        number = options['number']
        for i in range(number):
            User.objects.bulk_create([User(username=fake.name(),
                                           email=fake.email(),
                                           password=make_password(str(fake.password())))])
        self.stdout.write(self.style.SUCCESS('Create %s users successfully!' % number))
