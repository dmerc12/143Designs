from .models import Message
from django import forms

# Contact Form
class ContactForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name...'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name...'}))
    email = forms.EmailField(max_length=150, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@example.com'}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1-123-123-1234'}))
    title = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title for your message here...'}))
    message = forms.CharField(max_length=600, widget=forms.Textarea(attrs={'classs': 'form-control', 'placeholder': 'Enter your message here...', 'rows': '5'}))

    class Meta:
        model = Message
        fields = '__all__'
