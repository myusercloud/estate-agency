from django.contrib import admin
from django.urls import path
from getmoestate import views
from .views import appointment_list, appointment_create, appointment_update, appointment_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('agents/', views.agents, name='agents'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('appoint/', views.appoint, name='appoint'),
    path('property_details/', views.property_details, name='property_details'),
    path('appointment_list/', appointment_list, name='appointment_list'),
    path('create/', appointment_create, name='appointment_create'),
    path('<int:pk>/update/', appointment_update, name='appointment_update'),
    path('<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('<int:pk>/delete/', appointment_delete, name='appointment_delete'),
]