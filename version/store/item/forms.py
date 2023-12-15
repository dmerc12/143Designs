from django import forms
from .modals import Item

class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name']

class ItemUpdateForm(ItemCreateForm):
    class Meta:
        model = Item
        fields = ['name']
