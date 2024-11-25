from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EnquiryForm

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
            enquiry = form.save()

            subject = f"New Enquiry from {enquiry.enquiry_name}"
            message = f"""
            Enquiry Details:
            ID: {enquiry.enquiry_id}
            Name: {enquiry.enquiry_name}
            Email: {enquiry.enquiry_email}
            Occasion: {enquiry.enquiry_occasion}
            Location: {enquiry.enquiry_location}
            Theme: {enquiry.enquiry_theme}
            Date & Time: {enquiry.enquiry_when}
            Additional Info: {enquiry.enquiry_information}
            """
            recipient = settings.EMAIL_HOST_USER
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])

            messages.success(request, "Thank you for your enquiry! We should soon receive a reply from threeamigosquiz@gmail.com ")
            return redirect('enquiry:enquiry_form')

        else:
            messages.error(request, "Please fill in the required fields")
            return render(request, 'enquiry_form.html', {'form': form})
    
    else:
        form = EnquiryForm()

    return render(request, 'enquiry_form.html', {'form': form})