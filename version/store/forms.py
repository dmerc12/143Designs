from django import forms
from .models import Order, Item, OrderItem

class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name']

class ItemUpdateForm(ItemCreateForm):
    class Meta:
        model = Item
        fields = ['name']

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'description', 'paid', 'complete']

class OrderItemCreateForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['item', 'quantity']

OrderItemCreateFormSet = forms.inlineformset_factory(Order, OrderItem, form=OrderItemCreateForm, extra=1, can_delete=True)
