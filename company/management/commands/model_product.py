from django.core.management.base import BaseCommand
from company.serializers import ProductSerializer


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_data = {
            'name': 'Mahindra 575-DI Tractor',
            'company': 1,
            'price': 966000

        }
        serializer = ProductSerializer(data=user_data)
        if serializer.is_valid():
            product = serializer.save()
            print(f"Product created: {product}")
        else:
            print(serializer.errors)
