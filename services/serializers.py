from rest_framework import serializers
from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'price', 'duration',]  # noqa: RUF012

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value
    
    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError("Duration must be a positive integer.")
        return value