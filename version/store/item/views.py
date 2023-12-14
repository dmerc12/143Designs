from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ItemCreateForm
from .modals import Item


@login_required
def home(request):
    return render(request, 'store/home.html')

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemCreateForm()
    template_name = '/store/item/create.html'
    success_url = reversed('/store/')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        try:
            ItemMiddleware.create_item(name)
        except RuntimeError as error:
            form.add_error('name', str(error))
            return self.form_invalid(form)
        return super().form_valid(form)

class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'store/home.html'
    context_object_name = 'item'

    def get_items(self):
        return Item.objects.all()

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
