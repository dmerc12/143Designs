from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..forms import OrderItemForm

@login_required
def create_order_item(request):
    form = OrderItemForm()
    return render(request, 'store/order_item/form.html', {'order_item_form': form})
