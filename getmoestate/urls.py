
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from getmoestate import views
from .views import index, property_details, book_appointment, appointment_list, update_appointment, delete_appointment
from django.contrib.auth.decorators import login_required

admin.site.login = login_required(admin.site.login)
urlpatterns = [

    path('admin/', admin.site.urls),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('', views.index ,name='index'),
    path('property/<int:id>/', views.property_details, name='property_details'),
    path('propertydetails/', views.propertydetails, name='propertydetails'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('payment/', views.payment, name='payment'),
    path('agent/', views.agent, name='agent'),
    path('appointment/', views.appointment, name='appointment'),
    path('appointment_confirmation/', views.appointment_confirmation, name='appointment_confirmation'),
    path('propertydetailsdivein/', views.propertydetailsdivein, name='propertydetailsdivein'),
    path('property/create/', views.create_property, name='create_property'),
    path('property/<int:id>/edit/', views.update_property, name='update_property'),
    path('property/create/', views.create_property, name='create_property'),
    path('property/update/<int:id>/', views.update_property, name='update_property'),
    path('property/delete/<int:id>/', views.delete_property, name='delete_property'),
    path("appointment/", book_appointment, name="book_appointment"),
    path("appointments/", appointment_list, name="appointment_list"),
    path("appointment/update/<int:appointment_id>/", update_appointment, name="update_appointment"),
    path("appointment/delete/<int:appointment_id>/", delete_appointment, name="delete_appointment"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
