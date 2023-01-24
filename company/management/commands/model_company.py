from django.core.management.base import BaseCommand
from company.serializers import CompanySerializer
from company.models import Company


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_data = {
            'name': 'India Today Pvt Ltd',
            'owner': 16,

        }
        instance = Company.objects.get(pk=13)
        serializer = CompanySerializer(data=user_data, instance=instance)
        if serializer.is_valid():
            company = serializer.save()
            print(f"Company Created: {company}")
        else:
            print(serializer.errors)
