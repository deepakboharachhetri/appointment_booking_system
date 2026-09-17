from rest_framework import serializers
from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        read_only_fields = ['id', 'created_at', 'updated_at']  # noqa: RUF012
        fields = ['id', 'name', 'price', 'duration','created_at', 'updated_at']  # noqa: RUF012


    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative.")
        return value

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Service name cannot be blank.")
        return value.strip()
    
    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError("Duration must be a positive integer.")
        return value