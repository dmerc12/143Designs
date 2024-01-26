from django.contrib.auth.models import User, Group
from .models import Order, Item, Size
from django.contrib import admin

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(Size)

class ItemInline(admin.TabularInline):
    model = Order.item.through
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'short_description', 'total', 'complete', 'paid', 'last_modified', 'created']
    list_filter = ['created', 'last_modified', 'customer__first_name', 'customer__last_name', 'complete', 'paid', 'item']
    date_hierarchy = 'created'
    inlines = [ItemInline]
    fieldsets = (
        (None, {
            'fields': ('customer', 'short_description', 'description')
        }),
        ('Status', {
            'fields': ('complete', 'paid', 'total')
        }),
    )

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
