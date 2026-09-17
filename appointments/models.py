from django.db import models
from services.models import Service

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)
    service = models.ForeignKey('services.Service', on_delete=models.CASCADE)
    status= models.CharField(max_length=10, choices=STATUS_CHOICES, default='scheduled')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} - {self.service.name} on {self.appointment_date} at {self.appointment_time}"