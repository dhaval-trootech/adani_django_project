from django.core.management.base import BaseCommand
from company.serializers import CompanySerializer


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_data = {
            'name': 'Adani Airport Pvt Ltd',
            'owner': 1,

        }
        serializer = CompanySerializer(data=user_data)
        if serializer.is_valid():
            company = serializer.save()
            print(f"Company Created: {company}")
            print("FINAL APIVIEW+", serializer.data)
        else:
            print(serializer.errors)
