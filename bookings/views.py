from django.shortcuts import render
from .models import Booking

# Create your views here.

def get_index(request):
        return render(request, 'index.html')

def get_base(request):
        return render(request, 'base.html')

def get_dates(request):
        return render(request, 'dates.html')