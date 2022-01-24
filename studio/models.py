from enum import unique
from django.db import models
from django.http import request

class Booking(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    event_date = models.DateField(blank=True, null=True, unique=True, error_messages = {"unique":"Studio is already booked on that date. Please select a different date."})
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.request +" - [" + self.first_name + "]"
    
    class Meta:
        ordering = ["-sent_date"]