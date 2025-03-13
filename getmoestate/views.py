from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):  # Ensure this function exists
    return render(request, 'index.html')

def propertydetails(request):  # Ensure this function exists if needed
    return render(request, 'property-single.html')


def signup(request):  # Ensure this function exists if needed
    return render(request, 'signup.html')

def login(request):  # Ensure this function exists if needed
    return render(request, 'login.html')

def payment(request):  # Ensure this function exists if needed
    return render(request, 'payment.html')


def agent(request):  # Ensure this function exists if needed
    return render(request, 'agents.html')

def appointment(request):  # Ensure this function exists if needed
    return render(request, 'appointment.html')



def appointment_confirmation(request):  # Ensure this function exists if needed
    return render(request, 'appointment_confirmation.html')