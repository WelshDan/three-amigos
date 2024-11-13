from django.shortcuts import render, redirect, get_object_or_404
from .forms import EnquiryForm
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

def get_enquiry(request):
    return render(request, 'enquiry.html')

def error_404(request, exception):
    return render(request, '404.html')

def enquiry_form(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thanks for your enquiry. Our answer will be sent via email")

        else:
            return render(request, 'enquiry_form.html', {'form': form, 'error': 'Please fill in the necessary details'})
    
    else:
        form = EnquiryForm()

    return render(request, 'enquiry_form.html', {'form': form})