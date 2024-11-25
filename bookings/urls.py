from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.booking_form, name='booking_form'),
]