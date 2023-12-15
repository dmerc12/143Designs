from django.urls import path
from .item.views import ItemCreateView, ItemUpdateView, ItemDeleteView, ItemHomeView

urlpatterns = [
    path('', ItemHomeView.as_view(), name='store-home'),
    # path('item/<int:pk>/', ItemDetailView.as_view(), name='store-item-detail'),
    path('item/new/', ItemCreateView.as_view(), name='store-item-create'),
    path('item/<int:pk>/update/', ItemUpdateView.as_view(), name='store-item-update'),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name='store-item-delete'),
]
