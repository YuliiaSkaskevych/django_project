from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Delete users with helping entered their ID. Warning: you cant delete superuser!'

    def add_arguments(self, parser):
        parser.add_argument('users_id', nargs='+', type=int, help='Users ID to be deleted')

    def handle(self, *args, **options):
        user_id = options['users_id']
        users = User.objects.filter(pk__in=user_id, is_superuser=True)
        if not users.exists():
            User.objects.filter(pk__in=user_id).delete()
            self.stdout.write(self.style.SUCCESS('User %s deleted with success!' % user_id))
        else:
            self.stdout.write(self.style.ERROR('You enter ID superuser! Operation cant be continued!'))
