
from django.contrib import admin
from django.urls import path
from getmoestate import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', views.index),
]
