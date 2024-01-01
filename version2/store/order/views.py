from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import Order
from .middleware import OrderMiddleware

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order

class OrderDeleteView(LoginRequiredMixin,  DeleteView):
    model = Order
    template_name = 'store/order/delete.html'
    success_url = '/store'

    def delete(self, request):
        order = self.get_object()
        OrderMiddleware.delete_order(order.pk)
        messages.success(request, "Order deleted!")
        return redirect(self.success_url)
