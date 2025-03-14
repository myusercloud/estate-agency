from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100,default='Default Name')
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"
