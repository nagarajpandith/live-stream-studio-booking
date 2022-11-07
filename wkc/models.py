from django.db import models

class WKCBooking(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    event_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    request = models.CharField(max_length=50)
    sent_date = models.DateField(auto_now_add=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    # accepted = models.BooleanField(default=False)
    # rejected=models.BooleanField(default=False)
    # accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.request +" - [" + self.name + "]"
    
    class Meta:
        ordering = ["sent_date"]