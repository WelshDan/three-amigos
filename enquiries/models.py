from django.db import models
from django.utils import timezone


class Enquiry(models.Model):
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
        ('WP','Wirströms Pub (20-100ppl)'),
        ('W','At your workplace'),
        ('OL','Other Location'),
    )

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
    enquiry_location = models.CharField(
        max_length=30,
        choices=LOCATIONS,
        blank=True,
    )
    enquiry_number_of_quizzers = models.IntegerField(blank=True, null=True)
    enquiry_when = models.DateTimeField(default=timezone.now, null=False)
    enquiry_information = models.TextField(max_length=1000, blank=True)
    enquiry_sent = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Booking #{self.enquiry_id} - Name {self.enquiry_name} - Email {self.enquiry_email}"