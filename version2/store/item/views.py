from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Item, OrderItem
from django.contrib import messages
from ..forms import ItemForm

@login_required
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            current_items = Item.objects.filter(name=form.cleaned_data['name'])
            if current_items:
                messages.error('This item already exists, please try again!')
            else:
                item = Item(**form.cleaned_data)
                item.save()
                messages.success(request, 'Item successfully created!')
                return redirect('store-home')
    else:
        form = ItemForm()
    return render(request, 'store/item/create.html', {'form': form, 'action': 'create'})

@login_required
def update_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            current_items = Item.objects.filter(name=form.cleaned_data['name'])
            if current_items:
                messages.error(request, 'This item already exists, please try again!')
            else:
                form.save()
                messages.success(request, 'Item successfully updated!')
                return redirect('store-home')
    else:
        form = ItemForm(instance=item)
    return render(request, 'store/item/update.html', {'form': form, 'action': 'update', 'item': item})

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if not OrderItem.objects.filter(item=item).exists():
        if request.method == 'POST':
            item.delete()
            messages.success(request, 'Item successfully deleted!')
            return redirect('store-home')
    else:
        messages.error(request, 'Item is currently being used in an order and cannot be deleted!')
        return redirect('store-home')
    return render(request, 'store/item/delete.html', {'item': item})
