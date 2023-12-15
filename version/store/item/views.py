from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ItemCreateForm, ItemUpdateForm
from .modals import Item
from .middleware import ItemMiddleware

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemCreateForm
    template_name = 'store/item/create.html'
    success_url = '/store/'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        try:
            ItemMiddleware.create_item(name)
        except RuntimeError as error:
            form.add_error('name', str(error))
            return self.form_invalid(form)
        messages.success(self.request, f'Item created!')
        return redirect(self.success_url)

class ItemHomeView(LoginRequiredMixin, ListView):
    template_name = 'store/home.html'

    def get(self, request, *args, **kwargs):
        try:
            items = ItemMiddleware.get_all_items()
        except RuntimeError as error:
            items = []
            messages.warning(request, str(error))
        item_id = request.GET.get('selected_item')
        if not item_id and items:
            item_id = items[0].pk
        context = {
            'items': items,
            'item_id': item_id
        }
        return render(request, self.template_name, context)

# class ItemDetailView(LoginRequiredMixin, DetailView):
#     model = Item

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemUpdateForm
    template_name = 'store/item/update.html'
    success_url = '/store/'

    def form_valid(self, form):
        item_id = self.kwargs['pk']
        name = form.cleaned_data['name']
        try:
            ItemMiddleware.update_item(item_id, name)
        except RuntimeError as error:
            form.add_error('name', str(error))
            return self.form_invalid(form)
        messages.success(self.request, f'Item updated!')
        return redirect(self.success_url)

class ItemDeleteView(LoginRequiredMixin,  DeleteView):
    model = Item
    template_name = 'store/item/delete.html'
    success_url = '/store/'

    def delete(self, request, *args, **kwargs):
        item = self.get_object()
        ItemMiddleware.delete_item(item.pk)
        messages.success(request, "Item Deleted!")
        return super().delete(request, *args, **kwargs)
