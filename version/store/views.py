from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Item

@login_required
def home(request):
    return render(request, 'store/home.html')

class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'store/manage-items.html'
    context_object_name = 'items'

class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)

class ItemDeleteView(LoginRequiredMixin,  DeleteView):
    model = Item
    success_url = '/store/manage-items/'
