from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from ..forms import OrderItemForm
from..models import Order

@login_required
def create_order_item(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    form = OrderItemForm()
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            order_item = form.save(commit=False)
            order_item.order = order
            order_item.save()
            messages.success(request, 'Item successfully added to order!')
    else:
        return render(request, 'store/partials/form.html', {'item_form': form})
