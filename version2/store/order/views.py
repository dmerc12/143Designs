from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..forms import OrderForm, OrderItemForm
from django.contrib import messages
from ..models import Order, OrderItem

@login_required
def create_order(request):
    if request.method == 'POST':
        num_items = int(request.POST.get('num_items'))
        order_form = OrderForm(request.POST)
        order_item_forms = [OrderItemForm(request.POST) for i in range(0, num_items)]
        if order_form.is_valid()and [form.is_valid() for form in order_item_forms]:
            order = order_form.save()
            for item_form in order_item_forms:
                if item_form.cleaned_data:
                    item = item_form.cleaned_data['item']
                    quantity = item_form.cleaned_data['quantity']
                    OrderItem.objects.create(order=order, item=item, quantity=quantity)
            messages.success(request, 'Order successfully created!')
            return redirect('store-home')
    else:
        order_form = OrderForm()
        order_item_form = OrderItemForm()
    context = {
        'order_form': order_form, 
        'order_item_form': order_item_form
    }
    return render(request, 'store/order/create.html', context)

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
