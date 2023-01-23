from django.core.management.base import BaseCommand
from company.serializers import ProductSerializer


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_data = {
            'name': 'Adani Bags Combo',
            'company': 11,

        }
        serializer = ProductSerializer(data=user_data)
        if serializer.is_valid():
            product = serializer.save()
            print(f"Product created: {product}")
        else:
            print(serializer.errors)
