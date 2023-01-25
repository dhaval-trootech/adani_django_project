from rest_framework import serializers
from .models import User
import sqlparse
from django.db import connection


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'email', 'phone', 'confirm_password',
                  'is_superuser', 'is_staff')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_first_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("First name should only contain alphabet characters.")
        return value.capitalize()

    def validate_last_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Last name should only contain alphabet characters.")
        return value.capitalize()

    def validate_phone(self, value):
        if not len(str(value)) == 10:
            raise serializers.ValidationError("The phone number must contain only 10 digits.")
        return value

    # Last validation method
    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if not password == confirm_password:
            raise serializers.ValidationError("Password & Confirm Password Doesn't Matched..")
        del attrs['confirm_password']
        return attrs

    # Override Create() Method of ModelSerializer
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        query = connection.queries[-1]['sql']
        parsed = sqlparse.format(query, reindent=True, keyword_case='upper')
        print("SQL QUERY---> ", parsed)
        return user

    # Override Update() Method of ModelSerializer
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.set_password(validated_data.get('password'))
        instance.save()
        # to print SQl Query
        query = connection.queries[-1]['sql']
        parsed = sqlparse.format(query, reindent=True, keyword_case='upper')
        print("SQL QUERY---> ", parsed)
        return instance
