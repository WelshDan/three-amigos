from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm

# Create your views here.

def get_index(request):
    return render(request, 'index.html')

def get_base(request):
    return render(request, 'base.html')

def get_dates(request):
    return render(request, 'dates.html')

def get_results(request):
    return render(request, 'results.html')

def get_info(request):
    return render(request, 'info.html')

def get_enquiry(request):
    return render(request, 'enquiry.html')

def error_404(request, exception):
    return render(request, '404.html')

def booking_form(request):
    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save()

            subject = f"New Booking from {booking.booking_name}"
            message = f"""
            Enquiry Details:
            ID: {booking.booking_id}
            Name: {booking.booking_name}
            Email: {booking.booking_email}
            Occasion: {booking.booking_occasion}
            Location: {booking.booking_location}
            Theme: {booking.booking_theme}
            Date & Time: {booking.booking_when}
            Additional Info: {booking.booking_information}
            """
            recipient = settings.EMAIL_HOST_USER
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])

            messages.success(request, "Thank you for your enquiry! We should soon receive a reply from threeamigosquiz@gmail.com ")
            return redirect('booking:booking_form')

        else:
            messages.error(request, "Please fill in the required fields")
            return render(request, 'booking_form.html', {'form': form})
    
    else:
        form = BookingForm()

    return render(request, 'booking_form.html', {'form': form})