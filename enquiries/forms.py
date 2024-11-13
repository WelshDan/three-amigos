from django import forms
from .models import Enquiry

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = [
            'enquiry_name', 'enquiry_email', 'enquiry_company', 'enquiry_occasion',
            'enquiry_theme', 'enquiry_number_of_quizzers', 'enquiry_location', 
            'enquiry_when', 'enquiry_information']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Form fields initialized:", self.fields)