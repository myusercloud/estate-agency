
from django.contrib import admin
from django.urls import path
from getmoestate import views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index ,name='index'),
    path('propertydetails/', views.propertydetails, name='propertydetails'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('payment/', views.payment, name='payment'),
    path('agent/', views.agent, name='agent'),
    path('appointment/', views.appointment, name='appointment'),
    path('appointment_confirmation/', views.appointment_confirmation, name='appointment_confirmation'),
]
