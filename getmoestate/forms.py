from django import forms
from .models import Property, Appointment # Import your Property model

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price', 'location', 'image']



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['agent', 'client_name', 'client_email', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }