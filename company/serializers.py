from rest_framework import serializers
from .models import *
import sqlparse
from django.db import connection


# Serializer for Company - model /...
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'established_date', 'owner')

    # Override Create() Method of ModelSerializer
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        query = connection.queries[-1]['sql']
        parsed = sqlparse.format(query, reindent=True, keyword_case='upper')
        print("SQL QUERY---> ", parsed)
        return instance


# Serializer for Product - model /...
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'timestamps', 'company', 'category')


# Serializer for Category - model /...
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


# Serializer for Color - model /...
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('id', 'name')
