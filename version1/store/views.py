from django.shortcuts import render
from .models import Item

def home(request):
    items = Item.objects.all().order_by('-id')
    context = {
        'items': items
    }
    return render(request, 'home.html', context)
