from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib import messages

from .item.middleware import ItemMiddleware
from .order.middleware import OrderMiddleware
from .order_item.middleware import OrderItemMiddleware

from .models import Order
from .forms import OrderCreateForm, OrderItemCreateFormSet, OrderUpdateForm

class HomeView(LoginRequiredMixin, ListView):
    template_name = 'store/home.html'

    def get(self, request):
        try:
            items = ItemMiddleware.get_all_items()
            orders = OrderMiddleware.get_all_orders()
        except RuntimeError as error:
            items = []
            orders = []
            messages.warning(request, str(error))
        
        context = {
            'items': items,
            'orders': orders,
        }
        return render(request, self.template_name, context)

class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = 'store/order/create.html'
    success_url = '/store/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['order_items'] = OrderItemCreateFormSet(self.request.POST, instance=self.object)
        else:
            context['order_items'] = OrderItemCreateFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        order_items = context['order_items']

        if form.is_valid() and order_items.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            complete = form.cleaned_data['complete']
            paid = form.cleaned_data['paid']

            try:
                order = OrderMiddleware.create_order(name=name, description=description, complete=complete, paid=paid)
            except RuntimeError as error:
                form.add_error('name', str(error))
                return self.form_invalid(form)

            order_items.instance = order
            for order_item_form in order_items:
                if order_item_form.cleaned_data:
                    item = order_item_form.cleaned_data['item']
                    quantity = order_item_form.cleaned_data['quantity']

                    try:
                        OrderItemMiddleware.create_order_item(order=order, item=item, quantity=quantity)
                    except RuntimeError as error:
                        form.add_error(None, str(error))
                        return self.form_invalid(form)

            messages.success(self.request, "Order created!")
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderCreateForm
    template_name = 'store/order/update.html'
    success_url = '/store/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['order_items'] = OrderItemCreateFormSet(self.request.POST, instance=self.object)
        else:
            context['order_items'] = OrderItemCreateFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        order_items = context['order_items']

        if form.is_valid() and order_items.is_valid():
            order_id = self.kwargs['pk']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            complete = form.cleaned_data['complete']
            paid = form.cleaned_data['paid']

            try:
                order = OrderMiddleware.get_order(order_id)
                order.name = name
                order.description = description
                order.complete = complete
                order.paid = paid
                OrderMiddleware.update_order(order)
            except RuntimeError as error:
                form.add_error('name', str(error))
                return self.form_invalid(form)

            order_items.instance = order
            for order_item_form in order_items:
                if order_item_form.cleaned_data:
                    item = order_item_form.cleaned_data['item']
                    quantity = order_item_form.cleaned_data['quantity']

                    try:
                        OrderItemMiddleware.update_order_item(order=order, item=item, quantity=quantity)
                    except RuntimeError as error:
                        form.add_error(None, str(error))
                        return self.form_invalid(form)
            messages.success(self.request, "Order updated!")
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)
