from django.shortcuts import render
from .models import Booking

# Create your views here.

def get_index(request):
        return render(request, 'index.html')