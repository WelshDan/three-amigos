from django.db import models
from django.utils import timezone

REASONS = (
    ('AW','After Work'),
    ('KO','Work Kick Off'),
    ('BP','Birthday Party'),
    ('SP','Surprise Party'),
    ('O','Other'),
)

TYPES = (
    ('TAQ','Three Amigos Quiz'),
    ('S/T','Specific/Themed Quiz'),
)

LOCATIONS = (
    ('TS','The Snug (15-25ppl)'),
    ('WP','Wirströms Pub (25-100ppl)'),
    ('W','At your workplace'),
    ('OL','Other Location'),
)

class Booking(models.Model):
    booking_id = models.AutoField()
    name = models.CharField(max_length=150, blank= False)
    email = models.EmailField(max_length=150, unique=True, blank=False)
    company = models.CharField(max_length=150)
    reason = models.CharField(
        max_length=30,
        choices=REASONS,
        )
    quiz_type = models.CharField(
        max_length=20,
        choices=TYPES,
    )
    quizzers = models.IntegerField(max_length=3)
    where = models.CharField(
        max_length=30,
        choices=LOCATIONS,
    )
    when = models.DateTimeField()
    sent = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Booking #{self.booking_id} - Name {self.name} - Email {self.email}
                - Company {self.company} - Reason {self.reason} - Type of Quiz {self.quiz_type}
                - No.of Quizzers {self.quizzers} - Location {self.where} - Date/Time {self.when}"