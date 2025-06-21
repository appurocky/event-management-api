from django.db import models
from django.utils import timezone

class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_capacity = models.PositiveIntegerField()
    timezone = models.CharField(max_length=50, default='Asia/Kolkata')

    def __str__(self):
        return self.name

class Attendee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendees')

    class Meta:
        unique_together = ('email', 'event')  

    def __str__(self):
        return f"{self.name} ({self.email})"
