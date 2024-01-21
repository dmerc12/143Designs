from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..forms import OrderForm, OrderItemForm
from django.contrib import messages
from ..models import Order, OrderItem

@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            order_item_forms = request.POST.getlist('order_item_form')
            for item_form_data in order_item_forms:
                item_form = OrderItemForm(item_form_data)
                if item_form.is_valid():
                    order_item = OrderItem.objects.create(order=order, item=order_item.cleaned_data['item'], quantity=order_item.cleaned_data['quantity'])
            messages.success(request, 'Order successfully created!')
            return redirect('store-home')
    else:
        order_form = OrderForm()
        order_item_form = OrderItemForm()
    return render(request, 'store/order/create.html', {'order_form': order_form, 'order_item_form': order_item_form})

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
