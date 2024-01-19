from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..forms import OrderForm, OrderItemForm
from django.contrib import messages
from ..models import Order, OrderItem

@login_required
def create_order(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        order_item_forms = [OrderItemForm(request.POST, prefix=f'order_item_{i}') for i in range(1, 3)]
        if order_form.is_valid() and [form.is_valid() for form in order_item_forms]:
            order = order_form.save()
            for form in order_item_forms:
                if form.cleaned_data:
                    item = form.cleaned_data['item']
                    quantity = form.cleaned_data['quantity']
                    OrderItem.objects.create(item=item, quantity=quantity, order=order)
            messages.success(request, 'Order successfully created!')
            return redirect('store-home')
    else:
        order_form = OrderForm()
        order_item_forms = [OrderItemForm(prefix=f'order_item_{i}') for i in range(1, 3)]
    return render(request, 'store/order/create.html', {'order_form': order_form, 'order_item_forms': order_item_forms})

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
            order = form.save()
            messages.success(request, 'Order successfully updated!')
            return redirect('store-home')
    else:
        form = OrderForm(instance=order)
    return render(request, 'store/order/update.html', {'form': form, 'order': order})

@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        order.delete()
        messages.success(request, 'Order successfully deleted!')
        return redirect('store-home')
    return render(request, 'store/order/delete.html', {'order': order})
