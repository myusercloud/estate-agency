from django import forms
from .models import Appointment, Property

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price', 'location', 'image']