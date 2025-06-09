# accounts/serializers.py
from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'password', 'password2', 'is_company',
            'national_id', 'company_name', 'economic_code',
            'registration_number', 'postal_code', 'mobile'
        ]

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("رمز عبور و تکرارش برابر نیست.")

        if data.get('is_company'):
            required = ['company_name', 'economic_code', 'registration_number', 'postal_code']
            for field in required:
                if not data.get(field):
                    raise serializers.ValidationError({field: f"{field} برای شرکت الزامی است."})
        else:
            if not data.get('national_id'):
                raise serializers.ValidationError({'national_id': "کد ملی برای شخص حقیقی الزامی است."})

        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
