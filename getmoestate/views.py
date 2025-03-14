from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment
from .forms import AppointmentForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')


def agents(request):
    return render(request, 'agents.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def appoint(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment created successfully!")  # Success message
            return redirect('appointment_list')  # Redirect to the appointment list
    else:
        form = AppointmentForm()

    return render(request, 'appoint.html', {'form': form})

def property_details(request):
    return render(request, 'property-single.html'),

# List all appointments
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'list.html', {'appointments': appointments})

# Create a new appointment
def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_detail.html')
    else:
        form = AppointmentForm()
    return render(request, 'appoint.html', {'appoint': form})

# Update an existing appointment
def appointment_update(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_detail.html')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appoint.html', {'appoint': form})

# Delete an appointment
def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=
    pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_detail.html')
    return render(request, 'delete.html', {'appointment': appointment})

def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'appointment_detail.html', {'appointment': appointment})



