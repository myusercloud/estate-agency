from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='property_images/')
    listed_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Appointment(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments")
    client_name = models.CharField(max_length=255)
    client_email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()


    def __str__(self):
        return f"Appointment with {self.agent.username} on {self.date} at {self.time}"