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

OrderItemCreateFormSet = forms.inlineformset_factory(Order, OrderItem, fields=['item', 'quantity'], extra=1, can_delete=True)

class OrderUpdateForm(OrderCreateForm):
    orderitem_formset = forms.inlineformset_factory(Order, OrderItem, form=OrderItemCreateFormSet, extra=1, can_delete=True, fields=['item', 'quantity'])

    class Meta:
        model = Order
        fields = ['name', 'description', 'paid', 'complete']

    def __init__(self, *args, **kwargs):
        super(OrderUpdateForm, self).__init__(*args, **kwargs)
        self.orderitem_formset = self.orderitem_formset(instance=self.instance)

    def is_valid(self):
        return super(OrderUpdateForm, self).is_valid() and self.orderitem_formset.is_valid()

    def save(self, commit=True):
        saved_order = super(OrderUpdateForm, self).save(commit=commit)
        self.orderitem_formset.save()
        return saved_order
