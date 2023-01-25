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
            print(f"API based Beautiful data: {serializer.data}")
        else:
            print(serializer.errors)
