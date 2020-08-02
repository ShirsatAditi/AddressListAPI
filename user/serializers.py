from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


# Add new Address
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'address_line1','address_line2','city','pin_code','user_id')


# Add new Address
class ValidateAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = 'user_id'


# Add new Address
class GetAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'address_line1', 'address_line2', 'city', 'pin_code')

