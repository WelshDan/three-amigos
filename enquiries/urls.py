from django.urls import path
from . import views

app_name = 'enquiry'

urlpatterns = [
    path('', views.enquiry_form, name='enquiry_form'),
]