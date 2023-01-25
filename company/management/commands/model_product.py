from django.core.management.base import BaseCommand
from company.serializers import ProductSerializer


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_data = {
            'name': 'John Deer KING',
            'price': 1466000,
            'company': 1,
            'category': 17,
            'color': 2

        }
        serializer = ProductSerializer(data=user_data)
        if serializer.is_valid():
            product = serializer.save()
            print(f"Product created: {product}")
            print(f"API based Beautiful data: {serializer.data}")
        else:
            print(serializer.errors)
