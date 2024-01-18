from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..forms import OrderForm, OrderItemFormSet
from django.contrib import messages
from ..models import Order

@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        order_items = OrderItemFormSet(request.POST, instance=Order())
        if form.is_valid() and order_items.is_valid():
            saved_order = form.save(commit=False)
            order_items.instance = saved_order
            saved_order.save()
            order_items.save()
            messages.success(request, 'Order successfully created!')
            return redirect('store-home')
    else:
        form = OrderForm()
        order_items = OrderItemFormSet(instance=Order())
    return render(request, 'store/order/create.html', {'form': form})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'store/order/detail.html', {'order': order})

@login_required
def update_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order successfully updated!')
            return redirect('store-home')
    else:
        form = OrderForm(instance=order)
    return render(request, 'store/order/update.html', {'form': form})

@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        order.delete()
        messages.success(request, 'Order successfully deleted!')
        return redirect('store-home')
    return render(request, 'store/order/delete.html', {'order': order})
