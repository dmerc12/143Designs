from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from ..forms import OrderCreateForm, OrderUpdateForm
from ..models import Order
from .middleware import OrderMiddleware

class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = 'store/order/create.html'
    success_url = '/store/'

    def form_valid(self, form):
        # data fields, need to pass to create_order method
        try:
            OrderMiddleware.create_order()
        except RuntimeError as error:
            form.add_error('name', str(error))
            return self.form_invalid(form)
        messages.success(self.request, "Order created!")
        return redirect(self.success_url)

class OrderHomeView(LoginRequiredMixin, ListView):
    template_name = 'store/home.html'

    def get(self, request):
        try:
            orders = OrderMiddleware.get_all_orders()
        except RuntimeError as error:
            orders = []
            messages.warning(request, str(error))
        context = {
            'orders': orders,
        }
        return render(request, self.template_name, context)

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order

class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderUpdateForm
    template_name = 'store/order/update.html'
    success_url = '/store/'

    def form_valid(self, form):
        order_id = self.kwargs['pk']
        # data fields, need to pass to update_order method
        try:
            OrderMiddleware.update_order()
        except RuntimeError as error:
            form.add_error('name', str(error))
            return self.form_invalid(form)
        messages.success(self.request, "Order updated!")
        return redirect(self.success_url)

class OrderDeleteView(LoginRequiredMixin,  DeleteView):
    model = Order
    template_name = 'store/order/delete.html'
    success_url = '/store'

    def delete(self, request):
        order = self.get_object()
        OrderMiddleware.delete_order(order.pk)
        messages.success(request, "Order deleted!")
        return redirect(self.success_url)

