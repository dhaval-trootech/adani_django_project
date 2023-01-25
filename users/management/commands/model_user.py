from django.core.management.base import BaseCommand
from users.serializers import UserSerializer


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_data = {
            'username': 'satish10',
            'first_name': 'satish',
            'last_name': 'jain',
            'email': 'satish10@gmail.com',
            'phone': 7777777777,
            'password': 'Satish@123',
            'confirm_password': 'Satish@123',
            'is_staff': True

        }
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            user = serializer.save()
            print(f"User created: {user}")
            print(f"API based Beautiful data: {serializer.data}")
        else:
            print(serializer.errors)
