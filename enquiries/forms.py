from django import forms
from .models import Enquiry


class EnquiryForm(forms.ModelForm):

    enquiry_when = forms.DateTimeField(
    widget=forms.DateTimeInput(
        format='%d-%m-%Y %H:%M',
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
        model = Enquiry
        fields = [
            'enquiry_name', 'enquiry_email', 'enquiry_company', 'enquiry_occasion',
            'enquiry_theme', 'enquiry_number_of_quizzers', 'enquiry_location', 
            'enquiry_when', 'enquiry_information']