from django.core.management.base import BaseCommand
from company.serializers import SubCategorySerializer


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_data = {
            'name': 'coconut',
            'category': 10
        }
        serializer = SubCategorySerializer(data=user_data)
        if serializer.is_valid():
            category = serializer.save()
            print(f"Category created: {category}")
        else:
            print(serializer.errors)
