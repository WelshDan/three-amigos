from django.urls import path
from . import views

app_name = 'enquiry'

urlpatterns = [
    path('enquiry', views.get_enquiry, name='get_enquiry'),
    path('enquiry_form/', views.enquiry_form, name='enquiry_form'),
]