from site_management.models import Message
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
