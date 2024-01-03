from django import forms
from ..models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'text', 'rating']

    rating = forms.ChoiceField(choices=[(i / 2, str(i / 2)) for i in range(21)], widget=forms.RadioSelect)
