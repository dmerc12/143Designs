from django.urls import path
from .item.views import ItemCreateView, ItemUpdateView, ItemDeleteView
from .order.views import OrderDetailView, OrderDeleteView
from .views import HomeView, OrderCreateView, OrderUpdateView

urlpatterns = [
    path('', HomeView.as_view(), name='store-home'),
    # path('item/<int:pk>/', ItemDetailView.as_view(), name='store-item-detail'),
    path('item/new/', ItemCreateView.as_view(), name='store-item-create'),
    path('item/<int:pk>/update/', ItemUpdateView.as_view(), name='store-item-update'),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name='store-item-delete'),

    path('order/new/', OrderCreateView.as_view(), name='store-order-create'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='store-order-detail'),
    path('order/<int:pk>/update/', OrderUpdateView.as_view(), name='store-order-update'),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='store-order-delete'),
]
