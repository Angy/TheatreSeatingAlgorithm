from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create_superuser(
            username='testuser', email='test@user.com', password='password')
        self.stdout.write(f'User {user.email} created successfully')


