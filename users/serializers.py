from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    
    class Meta:
        model = CustomUser
        fields = [
            'first_name', 
            'last_name', 
            'username', 
            'email', 
            'password', 
            'company_name', 
            'number_of_outlets', 
            'number_of_employees', 
            'phone_number'
        ]
    
    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            company_name=validated_data.get('company_name', ''),
            number_of_outlets=validated_data.get('number_of_outlets', None),
            number_of_employees=validated_data.get('number_of_employees', None),
            phone_number=validated_data.get('phone_number', ''),
        )
        return user
