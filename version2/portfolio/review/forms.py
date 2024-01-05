from django import forms
from ..models import Review

class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'subject', 'text', 'rating']

class UpdateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'subject', 'text', 'rating', 'status']
