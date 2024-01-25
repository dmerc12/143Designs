from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..forms import CreateOrderForm, UpdateOrderForm, OrderItemForm
from django.contrib import messages
from ..models import Order, OrderItem

@login_required
def create_order(request):
    order_form = CreateOrderForm(request.POST or None)
    if request.method == 'POST':
        if order_form.is_valid():
            order_form.save()
            messages.success(request, 'Order successfully created!')
            return redirect('store-home')
    return render(request, 'store/order/create.html', {'order_form': order_form})

@login_required
def update_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order_form = UpdateOrderForm(request.POST or None, instance=order)
    order_items = OrderItem.objects.filter(order=order)
    item_forms = [OrderItemForm(instance=item) for item in order_items]
    context = {
        'item_forms': item_forms,
        'order_form': order_form,
        'order': order,
    }
    if order_form.is_valid():
        order = order_form.save()
        messages.success(request, 'Order Successfully Updated!')
        return redirect('store-order-update', order.pk)
    return render(request, 'store/order/update.html', context)

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'store/order/detail.html', {'order': order})

@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        order.delete()
        messages.success(request, 'Order successfully deleted!')
        return redirect('store-home')
    return render(request, 'store/order/delete.html', {'order': order})
