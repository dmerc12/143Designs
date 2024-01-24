from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..forms import OrderItemForm
from..models import Order

@login_required
def create_order_item(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    form = OrderItemForm(request.POST)
    if form.is_valid():
        order_item = form.save(commit=False)
        order_item.order = order
        order_item.save()
        messages.success(request, 'Item successfully added to order!')
        return redirect('store-order-update', order.pk)
        
@login_required
def add_new_form(request):
    form = OrderItemForm()
    return render(request, 'store/partials/form.html', {'item_form': form})
