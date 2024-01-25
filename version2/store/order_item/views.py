from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..forms import OrderItemForm
from..models import Order, OrderItem

@login_required
def get_item_form(request):
    return render(request, 'store/partials/form.html', {'item_form': OrderItemForm()})

@login_required
def create_order_item(request, order_id=0):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            order_item = form.save(commit=False)
            order_item.order = order
            order_item.save()
            messages.success(request, 'Item successfully added to order!')
            redirect('store-order-update', order.pk)
        else:
            return render(request, 'store/partials/form.html', {'item_form': form})
    else:
        return render(request, 'store/partials/form.html', {'item_form': OrderItemForm()})

@login_required
def update_order_item(request):
    pass
