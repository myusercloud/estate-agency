import json
from operator import truediv

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from requests.auth import HTTPBasicAuth
from getmoestate.models import *

from .credentials import MpesaAccessToken, LipanaMpesaPpassword
from .models import Appointment, Property
from .forms import AppointmentForm, PropertyForm
from django.contrib import messages
from django.contrib.auth.models  import User
from django.contrib.auth.decorators import user_passes_test, login_required

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')


def agents(request):
    return render(request, 'agents.html')


def panel(request):
    return render(request, 'admin_dashboard.html')


def is_admin(user):
    return user.is_authenticated and user.is_staff

def admin_signup(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return redirect('/login')
    return render(request, 'signup.html')

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

def property_single(request):
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

def contact(request):
    return render(request,'contact.html')


@login_required
def admin_dashboard(request):
    properties = Property.objects.all()
    return render(request, 'admin_dashboard.html', {'properties': properties})

@login_required
def add_property(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin_dashboard')
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})

@login_required
def update_property(request, id=id):
    property = get_object_or_404(Property, id=id)
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'update_property.html', {'form': form})

@login_required
def delete_property(request,id):
    property = get_object_or_404(Property, id=id)
    property.delete()
    return redirect('admin_dashboard')




def token(request):
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')

#Mpesa API
def stk(request):
    if request.method == "POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request_data = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "MedGet",
            "TransactionDesc": "Appointment Charges"
        }
        response = requests.post(api_url, json=request_data, headers=headers)

        # Parse response
        response_data = response.json()
        transaction_id = response_data.get("CheckoutRequestID", "N/A")
        result_code = response_data.get("ResponseCode", "1")  # 0 is success, 1 is failure

        # Save transaction to database
        transaction = Transaction(
            phone_number=phone,
            amount=amount,
            transaction_id=transaction_id,
            status="Success" if result_code == "0" else "Failed"
        )
        transaction.save()

        return HttpResponse(
            f"Transaction ID: {transaction_id}, Status: {'Success' if result_code == '0' else 'Failed'}")


def transactions_list(request):
    transactions = Transaction.objects.all().order_by('-date')
    return render(request, 'transactions.html', {'transactions': transactions})


