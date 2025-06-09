from rest_framework import serializers
from .models import InquiryRequest

class InquiryRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = InquiryRequest
        fields = '__all__'
        read_only_fields = ['user']

