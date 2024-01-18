from django import forms
from .models import Order, Item, OrderItem

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name']
        widgets = {
            'name': forms.TextInput()
        }

OrderItemFormSet = forms.formset_factory(Order, OrderItem, fields=['item', 'quantity'], extra=1, can_delete=False)

class OrderForm(forms.ModelForm):
    orderitem_formset = OrderItemFormSet

    class Meta:
        model = Order
        fields = ['name', 'description', 'paid', 'complete']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.orderitem_formset = self.orderitem_formset(instance=self.instance)

    def is_valid(self):
        return super(OrderForm, self).is_valid() and self.orderitem_formset.is_valid()

    def save(self, commit=True):
        saved_order = super(OrderForm, self).save(commit=commit)
        self.orderitem_formset.save()
        return saved_order
