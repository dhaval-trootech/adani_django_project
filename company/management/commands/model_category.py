from django.core.management.base import BaseCommand
from company.serializers import CategorySerializer


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_data = {
            'name': 'Women\'s shirts',
            'parent': 25
        }
        serializer = CategorySerializer(data=user_data)
        if serializer.is_valid():
            category = serializer.save()
            print(f"Category created: {category}")
            print(f"API based Beautiful data: {serializer.data}")
        else:
            print(serializer.errors)
