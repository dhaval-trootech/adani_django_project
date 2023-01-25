from django.core.management.base import BaseCommand
from company.serializers import CompanySerializer
from company.models import Company


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_data = {
            'name': 'Chandigarh Pharma Ltd',
            'owner': 2,

        }
        serializer = CompanySerializer(data=user_data)
        if serializer.is_valid():
            company = serializer.save()
            print(f"Company Created: {company}")
            print(f"API based Beautiful data: {serializer.data}")
        else:
            print(serializer.errors)
