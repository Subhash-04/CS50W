from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Profile

class Command(BaseCommand):
    help = 'Create profiles for all users'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            Profile.objects.get_or_create(user=user)
        self.stdout.write(self.style.SUCCESS('Successfully created profiles for all users'))
