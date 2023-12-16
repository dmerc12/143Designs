from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from ..forms import OrderItemCreateForm
from ..models import OrderItem
from .middleware import OrderItemMiddleware

class OrderItemCreateView(LoginRequiredMixin, CreateView):
    model = OrderItem
    form_class = OrderItemCreateForm
    template_name = 'store/order-item/create.html'
    success_url = '/store/'

    def form_valid(self, form):
        # data fields, need to pass to create_order_item method
        try:
            OrderItemMiddleware.create_order_item()
        except RuntimeError as error:
            form.add_error('name', str(error))
            return self.form_invalid(form)
        messages.success(self.request, "Order Item created!")
        return redirect(self.success_url)

class OrderItemHomeView(LoginRequiredMixin, ListView):
    template_name = 'store/home.html'

    def get(self, request):
        try:
            order_items = OrderItemMiddleware.get_all_order_items()
        except RuntimeError as error:
            order_items = []
            messages.warning(request, str(error))
        context = {
            'order_items': order_items,
        }
        return render(request, self.template_name, context)

class OrderItemDetailView(LoginRequiredMixin, DetailView):
    model = OrderItem

class OrderItemUpdateView(LoginRequiredMixin, UpdateView):
    model = OrderItem
    form_class = 0 # update order item form class, 0 is just a placeholder value
    template_name = 'store/order-item/update.html'
    success_url = '/store/'

    def form_valid(self, form):
        order_item_id = self.kwargs['pk']
        # data fields, need to pass to update_order method
        try:
            OrderItemMiddleware.update_order_item()
        except RuntimeError as error:
            form.add_error('name', str(error))
            return self.form_invalid(form)
        messages.success(self.request, "Order Item updated!")
        return redirect(self.success_url)

class OrderItemDeleteView(LoginRequiredMixin,  DeleteView):
    model = OrderItem
    template_name = 'store/order-item/delete.html'
    success_url = '/store'

    def delete(self, request):
        order_item = self.get_object()
        OrderItemMiddleware.delete_order_item(order_item.pk)
        messages.success(request, "Order Item deleted!")
        return redirect(self.success_url)

