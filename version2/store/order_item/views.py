from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ..forms import OrderItemForm
from ..models import OrderItem

def create_order_item(request):
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'store/order_item/form.html', {'form': OrderItemForm()})
