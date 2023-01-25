from django.core.management.base import BaseCommand
from company.serializers import CompanySerializer
from company.models import Company


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_data = {
            'name': 'Tata Industries Pvt Ltd',
            'owner': 4,

        }
        serializer = CompanySerializer(data=user_data)
        if serializer.is_valid():
            company = serializer.save()
            print(f"Company Created: {company}")
        else:
            print(serializer.errors)
