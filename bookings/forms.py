from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    booking_when = forms.DateTimeField(
        widget=forms.DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'}
        ),
        label="Preferred Date and Time"
    )

    OCCASIONS = (
        ('AW','After Work'),
        ('KO','Work Kick Off'),
        ('BP','Birthday Party'),
        ('SP','Surprise Party'),
        ('O','Other'),
    )

    THEMES = (
        ('TAQ','Three Amigos Quiz'),
        ('ST','Specific/Themed Quiz'),
    )

    LOCATIONS = (
        ('TS','The Snug (12-20ppl)'),
        ('WP','Wirströms Pub (25-100ppl)'),
        ('W','At your workplace'),
        ('OL','Other Location'),
    )


    class Meta:
        model = Booking
        fields = [
            'booking_name', 'booking_email', 'booking_company', 'booking_occasion',
            'booking_theme', 'booking_number_of_quizzers', 'booking_location', 
            'booking_when', 'booking_information']