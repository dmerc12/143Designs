from django.contrib.auth.models import User, Group
from .models import Order, Item, OrderItem
from django.contrib import admin

admin.site.unregister(Group)
admin.site.unregister(User)

class ItemInline(admin.TabularInline):
    model = Order.item.through
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ItemInline]

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
