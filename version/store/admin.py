from django.contrib import admin
from .item.modals import Item
from .order.modals import Order
from .order_item.modals import OrderItem

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
