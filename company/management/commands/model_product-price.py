from django.core.management.base import BaseCommand
from company.serializers import ProductPriceSerializer


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_data = {
            'price': 1299,
            'product': 1,

        }
        serializer = ProductPriceSerializer(data=user_data)
        if serializer.is_valid():
            productPrice = serializer.save()
            print(f"User created: {productPrice}")
        else:
            print(serializer.errors)
