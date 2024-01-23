from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..forms import OrderForm, OrderItemForm, OrderItemFormSet
from django.contrib import messages
from ..models import Order, OrderItem

@login_required
def create_order(request):
    order_form = OrderForm(request.POST or None)
    item_forms = OrderItemFormSet(request.POST or None, queryset=OrderItem.objects.none())
    context = {
        'order_form': order_form,
        'item_forms': item_forms
    }
    if request.htmx:
        form = item_forms.empty_form
        return render(request, 'store/partials/form.html', {'form':form})
    if all([order_form.is_valid(), item_forms.is_valid()]):
        order = order_form.save()
        for form in item_forms:
            item = form.save(commit=False)
            item.order = order
            item.save()
        messages.success(request, 'Order Successfully Created!')
        return redirect('store-home')
    return render(request, 'store/order/create.html', context)

@login_required
def update_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order_form = OrderForm(request.POST or None, instance=order)
    item_forms = OrderItemFormSet(request.POST or None, queryset=OrderItem.objects.filter(order=order))
    context = {
        'item_forms': item_forms,
        'order_form': order_form,
        'order': order
    }
    if all([order_form.is_valid(), item_forms.is_valid()]):
        order = order_form.save()
        for form in item_forms:
            item = form.save(commit=False)
            if item.order == None:
                item.order = order
            item.save()
        messages.success(request, 'Order Successfully Updated!')
        return redirect('store-home')
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
