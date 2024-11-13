from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from django.http import HttpResponse


# Create your views here.

def get_index(request):
    return render(request, 'index.html')

def get_base(request):
    return render(request, 'base.html')

def get_dates(request):
    return render(request, 'dates.html')

def get_results(request):
    return render(request, 'results.html')

def error_404(request, exception):
    return render(request, '404.html')
