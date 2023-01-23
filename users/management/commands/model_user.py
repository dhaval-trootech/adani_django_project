from django.core.management.base import BaseCommand
from users.serializers import UserSerializer


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_data = {
            'username': 'deep10',
            'first_name': 'Deep',
            'last_name': 'Patel',
            'email': 'jatin10@gmail.com',
            'phone': 8474672341,
            'password': 'Deep@12911',
            'confirm_password': 'Deep@12911'

        }
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            user = serializer.save()
            print(f"User created: {user}")
        else:
            print(serializer.errors)
