from django.contrib import admin
from.models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'booking_name', 'booking_email', 'booking_company',
        'booking_occasion','booking_theme', 'booking_number_of_quizzers', 
        'booking_location', 'booking_when')
    search_fields = ('booking_name', 'booking_email', 'booking_location', 'booking_when')