from django.core.management.base import BaseCommand
from users.serializers import UserSerializer
from users.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        user_data = {
            'username': 'aroon10',
            'first_name': 'Aroon',
            'email': 'aroon10@gmail.com',
            'phone': 1234567890,
            'password': 'Aroon@12911',
            'confirm_password': 'Aroon@12911',

        }
        instance = User.objects.get(pk=16)
        serializer = UserSerializer(data=user_data, instance=instance)
        if serializer.is_valid():
            user = serializer.save()
            print(f"User created: {user}")
        else:
            print(serializer.errors)
