from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..forms import OrderForm, OrderItemFormSet
from django.contrib import messages
from ..models import Order, OrderItem

@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        formset = OrderItemFormSet(request.POST, queryset=OrderItem.objects.none())
        if form.is_valid() and formset.is_valid():
            order = form.save(commit=False)
            order.save()
            for form in formset:
                OrderItem.objects.create(order=order, **form.cleaned_data)
            messages.success(request, 'Order successfully created!')
            return redirect('store-home')
    else:
        form = OrderForm()
    formset = OrderItemFormSet()
    return render(request, 'store/order/create.html', {'form': form, 'formset': formset})

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
