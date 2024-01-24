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

class CreateOrderForm(forms.ModelForm):
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

class UpdateOrderForm(forms.ModelForm):
    error_class = 'error-field'
    required_field = 'required-field'
    class Meta:
        model = Order
        fields = ['name', 'description', 'paid', 'complete', 'total']

    def __init__(self, * args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Customer Name'
        self.fields['name'].widget.attrs.update({'class': 'form-control col-9', 'placeholder': 'Customer Name'})
        self.fields['description'].label = 'Order Description'
        self.fields['description'].widget.attrs.update({'class': 'form-control col-lg-11 ml-2', 'placeholder': 'Order Description', 'cols': '5', 'rows': '4'})
        self.fields['total'].label = 'Order Total'
        self.fields['total'].widget.attrs.update({'class': 'form-control col-9', 'placeholder': 'Order Total'})

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
