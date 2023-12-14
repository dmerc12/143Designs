from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ItemCreateForm
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
        return redirect(self.success_url)

class ItemHomeView(LoginRequiredMixin, ListView):
    template_name = 'store/home.html'

    def get(self, request, *args, **kwargs):
        items = ItemMiddleware.get_all_items()
        selected_item = request.GET.get('selected_item', '')
        show_buttons = selected_item != ''
        context = {
            'items': items,
            'show_buttons': show_buttons,
            'selected_item': selected_item
        }
        return render(request, self.template_name, context)

class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)

class ItemDeleteView(LoginRequiredMixin,  DeleteView):
    model = Item
    success_url = '/store/manage-item/'