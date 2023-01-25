from django.core.management.base import BaseCommand
from users.serializers import UserSerializer


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_data = {
            'username': 'ratan10',
            'first_name': 'ratan',
            'last_name': 'tata',
            'email': 'ratan10@gmail.com',
            'phone': 9999999999,
            'password': 'Ratan@123',
            'confirm_password': 'Ratan@123',
            'is_superuser': True

        }
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            user = serializer.save()
            print(f"User created: {user}")
        else:
            print(serializer.errors)
