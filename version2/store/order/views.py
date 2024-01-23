from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..forms import OrderForm, OrderItemFormSet
from django.contrib import messages
from ..models import Order, OrderItem, Item
from django.forms import inlineformset_factory
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db import transaction

class CreateOrder(CreateView, LoginRequiredMixin):
    model = Order
    fields = ['name', 'description', 'paid', 'complete']
    template_name = 'store/order/create.html'
    success_url = reverse_lazy('store-home')

    def get_context_data(self, **kwargs):
        data = super(CreateOrder, self).get_context_data(**kwargs)
        if self.request.POST:
            data['items'] = OrderItemFormSet(self.request.POST, instance=self.object, extra=1)
        else:
            data['items'] = OrderItemFormSet(instance=self.object, queryset=OrderItem.objects.none())
        return data
    
    def form_valid(self, form):
        context = self.get_context_data()
        items = context['items']
        with transaction.atomic():
            self.object = form.save()

            if items.is_valid():
                items.instance = self.object
                items.save()

        return super(CreateOrder, self).form_valid(form)

# @login_required
# def create_order(request):
#     OrderItemFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm)

#     order_form = OrderForm()
#     order_item_forms = OrderItemFormSet(instance=Order())

#     if request.method == 'POST':
#         order_form = OrderForm(request.POST)
#         order_item_forms = OrderItemFormSet(request.POST, instance=Order())

#         if order_form.is_valid() and order_item_forms.is_valid():
#             order = order_form.save(commit=False)
#             order.save()

#             for item_form in order_item_forms:
#                 if item_form.cleaned_data:
#                     item = item_form.cleaned_data['item']
#                     quantity = item_form.cleaned_data['quantity']
#                     OrderItem.objects.create(order=order, item=item, quantity=quantity)

#             messages.success(request, 'Order successfully created!')
#             return redirect('store-home')

#     context = {
#         'order_form': order_form,
#         'order_item_forms': order_item_forms
#     }
#     return render(request, 'store/order/create.html', context)

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
