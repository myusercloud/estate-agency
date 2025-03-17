from django.contrib import admin
from django.urls import path
from getmoestate import views
from .views import appointment_list, appointment_create, appointment_update, appointment_delete, appointment_detail
from . import views
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('agents/', views.agents, name='agents'),
    path('contact/', views.contact, name='contact'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_panel/', views.panel, name='panel'),
    path('appoint/', views.appoint, name='appoint'),
    path('add_property/', views.add_property, name='add_property'),
    path('property-single/', views.property_single, name='property-single'),
    path('appointment_list/', appointment_list, name='appointment_list'),
    path('appointment_detail/', appointment_detail, name='appointment_detail'),
    path('create/', appointment_create, name='appointment_create'),
    path('<int:pk>/update/', appointment_update, name='appointment_update'),
    path('<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('<int:pk>/delete/', appointment_delete, name='appointment_delete'),

    # Mpesa API
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('transactions/', views.transactions_list, name='transactions'),

    path('edit/<int:id>/', views.update_property, name='edit'),
    path('delete/<int:id>/', views.delete_property ),
]