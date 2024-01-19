from django import forms
from .models import Order, Item, OrderItem

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name']
        widgets = {
            'name': forms.TextInput()
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'description', 'paid', 'complete']

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['item', 'quantity']
