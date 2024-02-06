from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Item

# Index route into the store portion of the website
def store_home(request):
    items = Item.objects.filter(featured=True)
    context = {'items': items}
    return render(request, 'store/index.html', context)

# Detail page for an item in the store
def item_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    related_items = Item.objects.filter(category=item.category).exclude(id=item.id).order_by('?')[:4]
    sizes = {}
    for size in item.product.get_product_sizes():
        size_price = size.price + item.design.price
        sizes[size.size] = size_price
    sizes = dict(sorted(sizes.items(), key=lambda item: item[1]))
    context = {
        'item': item,
        'sizes': sizes,
        'related_items': related_items
    }
    return render(request, 'store/detail.html', context)
