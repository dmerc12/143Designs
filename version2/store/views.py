from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Order, Item

@login_required
def home(request):
    items = Item.objects.all()
    orders = Order.objects.all()
    context = {
        'items': items,
        'orders': orders
    }
    return render(request, 'store/home.html', context)
    