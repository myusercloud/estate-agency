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



class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='property_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

#Mpesa API
class Transaction(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.amount} - {self.status}"