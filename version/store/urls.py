from django.urls import path
from .views import ItemListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='store-home'),
    path('manage-items/', ItemListView.as_view(), name='store-manage-items'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='store-item-detail'),
    path('item/new/', ItemCreateView.as_view(), name='store-item-create'),
    path('item/<int:pk>/update/', ItemUpdateView.as_view(), name='store-item-update'),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name='store-item-delete'),
]
