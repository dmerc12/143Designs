from django import forms
from .models import Order, Item, OrderItem

class ItemForm(forms.ModelForm):
    error_class = 'error-field'
    required_field = 'required-field'
    class Meta:
        model = Item
        fields = ['name']
        widgets = {
            'name': forms.TextInput()
        }

    def __init__(self, * args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Item Name'
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Item Name'})

class OrderForm(forms.ModelForm):
    error_class = 'error-field'
    required_field = 'required-field'
    class Meta:
        model = Order
        fields = ['name', 'description', 'paid', 'complete']

    def __init__(self, * args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Customer Name'
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Customer Name'})
        self.fields['description'].label = 'Order Description'
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Order Description', 'cols': '5', 'rows': '4'})

class OrderItemForm(forms.ModelForm):
    error_class = 'error-field'
    required_field = 'required-field'
    class Meta:
        model = OrderItem
        fields = ['item', 'quantity']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Quantity'})

OrderItemFormSet = forms.modelformset_factory(OrderItem, form=OrderItemForm, extra=0)
