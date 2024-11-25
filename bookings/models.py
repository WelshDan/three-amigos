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
    booking_location = models.CharField(
        max_length=30,
        choices=LOCATIONS,
        blank= False,
    )
    booking_number_of_quizzers = models.IntegerField()
    booking_when = models.DateTimeField(default=timezone.now, blank= False)
    booking_information = models.TextField(max_length=1000, blank=True)
    booking_sent = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Booking #{self.booking_id} - Name {self.booking_name} - Email {self.booking_email}"
