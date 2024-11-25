# Generated by Django 4.2.13 on 2024-11-25 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0008_booking_booking_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_location',
            field=models.CharField(choices=[('TS', 'The Snug (12-20ppl)'), ('WP', 'Wirströms Pub (20-100ppl)'), ('W', 'At your workplace'), ('OL', 'Other Location')], max_length=30),
        ),
    ]