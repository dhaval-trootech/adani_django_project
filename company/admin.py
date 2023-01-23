from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'established_date', 'owner')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company')


@admin.register(ProductPrice)
class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'timestamp')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product')


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'color')
