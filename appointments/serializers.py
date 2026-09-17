from django.utils import timezone
from rest_framework import serializers

from services.models import Service

from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())

    class Meta:
        model = Appointment
        read_only_fields = ['id', 'created_at', 'updated_at']  # noqa: RUF012
        fields = ['id', 'customer_name', 'customer_phone', 'service','status' , 'appointment_date', 'appointment_time', 'notes','created_at', 'updated_at']  # noqa: RUF012

    def validate_appointment_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Appointment date cannot be in the past.")
        return value

    def validate_appointment_time(self, value):
        if self.initial_data.get('appointment_date') == str(timezone.now().date()) and value < timezone.now().time():
            raise serializers.ValidationError("Appointment time cannot be in the past.")
        return value

    def validate_service(self, value):
        if not Service.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Selected service does not exist.")
        return value

    def validate_status(self, value):
        valid_statuses = [choice[0] for choice in Appointment.STATUS_CHOICES]
        if value not in valid_statuses:
            raise serializers.ValidationError(f"Status must be one of {valid_statuses}.")
        return value

    def validate(self, attrs):
        conflict = Appointment.objects.filter(
            appointment_date=attrs.get('appointment_date'),
            appointment_time=attrs.get('appointment_time')
        ) 
        if conflict:
            raise serializers.ValidationError("This time slot is already booked for the selected doctor.")

