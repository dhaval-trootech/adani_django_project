from rest_framework import serializers
from .models import User
import sqlparse
from django.db import connection


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'password', 'email', 'phone', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_email(self, value):
        return value

    def validate_first_name(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("The first letter of the first name must be uppercase.")
        elif not value.isalpha():
            raise serializers.ValidationError("First name should only contain alphabet characters.")
        return value

    def validate_last_name(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("The first letter of the last name must be uppercase.")
        elif not value.isalpha():
            raise serializers.ValidationError("Last name should only contain alphabet characters.")
        return value

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
        return attrs

    # Override Create() Method of ModelSerializer
    def create(self, validated_data):
        del validated_data['confirm_password']
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
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
