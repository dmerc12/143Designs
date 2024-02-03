from site_management.models import Message
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'title', 'message']
