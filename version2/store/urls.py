from django.urls import path
from .item import views as item_views
from .order import views as order_views
from . import views 

urlpatterns = [
    path('', views.home, name='store-home'),
    path('item/new/', item_views.create_item, name='store-item-create'),
    path('item/<int:item_id>/update/', item_views.update_item, name='store-item-update'),
    path('item/<int:item_id>/delete/', item_views.delete_item, name='store-item-delete'),

    path('order/new/', order_views.create_order, name='store-order-create'),
    path('order/<int:order_id>/', order_views.order_detail, name='store-order-detail'),
    path('order/<int:order_id>/update/', order_views.update_order, name='store-order-update'),
    path('order/<int:order_id>/delete/', order_views.delete_order, name='store-order-delete'),
]
