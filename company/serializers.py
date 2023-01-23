from rest_framework import serializers
from .models import *


# Serializer for Company - model /...
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'established_date', 'owner')


# Serializer for Product - model /...
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'company')


# Serializer for ProductPrice - model /...
class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = ('id', 'product', 'price')


# Serializer for Category - model /...
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'product')


# Serializer for Color - model /...
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('id', 'name')
