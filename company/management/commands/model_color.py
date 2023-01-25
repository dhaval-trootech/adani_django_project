from django.core.management.base import BaseCommand
from company.serializers import ColorSerializer


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_data = {
            'name': 'Brownish Black'
        }
        serializer = ColorSerializer(data=user_data)
        if serializer.is_valid():
            color = serializer.save()
            print(f"Color created: {color}")
        else:
            print(serializer.errors)
