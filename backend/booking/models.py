from django.db import models

class Appointment(models.Model):
    date = models.DateField()
    time = models.CharField(max_length=5)  # e.g., "10:30"
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    class Meta:
        unique_together = ('date', 'time')  # Prevent double-booking