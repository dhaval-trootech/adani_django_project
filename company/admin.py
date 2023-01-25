from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'established_date', 'owner')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'timestamp', 'company', 'category', 'color')

    # Overriding Products QuerySet, Only the current login user can see their own products.
    def get_queryset(self, request):
        queryset = super().get_queryset(request)  # TODO:nxcvbcx
        if request.user.is_superuser:
            return queryset
        companies = Company.objects.filter(owner=request.user)
        return queryset.filter(company__in=companies)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent')


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
