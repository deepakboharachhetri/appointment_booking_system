from django.db import models
from services.models import Service



class Appointment(models.Model):
    STATUS_CHOICES = [  # noqa: RUF012
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    customer_name = models.CharField(max_length=510)
    customer_phone = models.CharField(max_length=15)
    service = models.ForeignKey('services.Service', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        constraints = [  # noqa: RUF012
            models.UniqueConstraint(
                fields=['appointment_date', 'appointment_time'],
                name='unique_slot',
            ),
        ]

    def __str__(self):
        return f"{self.customer_name} - {self.service.name} on {self.appointment_date} at {self.appointment_time}"