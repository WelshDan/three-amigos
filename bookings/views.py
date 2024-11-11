from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking, OCCASIONS, THEMES, LOCATIONS

# Create your views here.

def get_index(request):
    return render(request, 'index.html')

def get_base(request):
    return render(request, 'base.html')

def get_dates(request):
    return render(request, 'dates.html')

def get_results(request):
    return render(request, 'results.html')

def get_enquiry(request):
    return render(request, 'enquiry.html')

def error_404(request, exception):
    return render(request, '404.html')

def enquiry_form(request):
    context = {
            'locations': LOCATIONS,
            'occasions': OCCASIONS,
            'themes': THEMES,
    }
    return render(request, 'enquiry.html', context)