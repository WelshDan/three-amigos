from django.urls import path
from bookings import views

app_name = 'bookings'
urlpatterns = [
    path('enquiry_form/', views.enquiry_form, name='enquiry_form'),
]