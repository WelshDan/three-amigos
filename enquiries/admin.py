from django.contrib import admin
from.models import Enquiry
# Register your models here.

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('enquiry_id', 'enquiry_name', 'enquiry_email', 'enquiry_company',
        'enquiry_occasion','enquiry_theme', 'enquiry_number_of_quizzers', 
        'enquiry_location', 'enquiry_when')
    search_fields = ('enquiry_name', 'enquiry_email', 'enquiry_location', 'enquiry_when')