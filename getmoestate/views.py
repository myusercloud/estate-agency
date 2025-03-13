import json
from django.contrib.auth.decorators import login_required, user_passes_test
import requests
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import PropertyForm, AppointmentForm

# Create your views here.


def index(request):
    properties = Property.objects.all()
    return render(request, 'index.html', {'properties': properties})

def property_details(request, id):
    property = get_object_or_404(Property, id=id)
    return render(request, 'property_details.html', {'property': property})

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

def propertydetailsdivein(request):  # Ensure this function exists if needed
    return render(request, 'property_details_dive_in.html')


def is_admin(user):
    return user.is_authenticated and user.is_superuser

# Create Property (Admin only)
@login_required
@user_passes_test(is_admin)
def create_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('property_list')  # Update with the actual URL name
    else:
        form = PropertyForm()
    return render(request, 'property_form.html', {'form': form})

# Update Property
@login_required
@user_passes_test(is_admin)
def update_property(request, id):
    property = get_object_or_404(Property, id=id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'property_form.html', {'form': form})

# Delete Property
@login_required
@user_passes_test(is_admin)
def delete_property(request, id):
    property = get_object_or_404(Property, id=id)
    if request.method == "POST":
        property.delete()
        return redirect('property_list')
    return render(request, 'property_confirm_delete.html', {'property': property})




@login_required
@user_passes_test(is_admin)  # Ensure only admins can access
def admin_dashboard(request):
    properties = Property.objects.all()
    return render(request, 'admin_dashboard.html', {'properties': properties})




def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("appointment_list.html")  # Redirect to list view
    else:
        form = AppointmentForm()
    return render(request, "book_appointment.html", {"form": form})



def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, "appointments/appointment_list.html", {"appointments": appointments})



def update_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect("appointment_list")
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, "appointments/update_appointment.html", {"form": form})

def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == "POST":
        appointment.delete()
        return redirect("appointment_list")
    return render(request, "appointments/delete_appointment.html", {"appointment": appointment})

