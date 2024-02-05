from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Item

def store_home(request):
    items = Item.objects.filter(featured=True)
    context = {'items': items}
    return render(request, 'store/index.html', context)
