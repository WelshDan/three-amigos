from django.db import models
from django.utils import timezone

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

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    booking_name = models.CharField(max_length=150, blank= False)
    booking_email = models.EmailField(max_length=150, blank= False)
    booking_company = models.CharField(max_length=150)
    booking_occasion = models.CharField(
        max_length=30,
        choices=OCCASIONS,
        blank= False,
        )
    booking_theme = models.CharField(
        max_length=20,
        choices=THEMES,
        blank= False,
    )
    booking_number_of_quizzers = models.IntegerField()
    booking_location = models.CharField(
        max_length=30,
        choices=LOCATIONS,
        blank= False,
    )
    booking_when = models.DateTimeField(default=timezone.now, blank= False)
    booking_sent = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Booking #{self.booking_id} - Name {self.booking_name} - Email {self.booking_email}"


class Enquiry(models.Model):
    enquiry_id = models.AutoField(primary_key=True)
    enquiry_name = models.CharField(max_length=150, blank= False)
    enquiry_email = models.EmailField(max_length=150, blank=False)
    enquiry_company = models.CharField(max_length=150, blank=True)
    enquiry_occasion = models.CharField(
        max_length=30,
        choices=OCCASIONS,
        blank=True,
        )
    enquiry_theme = models.CharField(
        max_length=20,
        choices=THEMES,
        blank=True,
    )
    enquiry_number_of_quizzers = models.IntegerField(blank=True, null=True)
    enquiry_location = models.CharField(
        max_length=30,
        choices=LOCATIONS,
        blank=True,
    )
    enquiry_when = models.DateTimeField(default=timezone.now, blank=True, null=True)
    enquiry_information = models.TextField(max_length=1000, blank=True)
    enquiry_sent = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Booking #{self.enquiry_id} - Name {self.enquiry_name} - Email {self.enquiry_email}"