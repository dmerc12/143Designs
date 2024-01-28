from django.contrib.auth.models import User, Group
from django.contrib import admin
from .models import Order

admin.site.unregister(Group)
admin.site.unregister(User)

class ProductInline(admin.TabularInline):
    model = Order.item.through
    extra = 1
    verbose_name = 'Item'
    verbose_name_plural = 'Items'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'short_description', 'total', 'complete', 'paid', 'last_modified', 'created']
    list_filter = ['created', 'last_modified', 'customer__first_name', 'customer__last_name', 'complete', 'paid', 'item']
    search_fields = ['created', 'last_modified', 'id', 'customer__first_name', 'customer__last_name', 'customer__email', 'customer__phone_number']
    date_hierarchy = 'created'
    inlines = [ProductInline]
    fieldsets = (
        (None, {
            'fields': ('customer', 'short_description', 'description')
        }),
        ('Status', {
            'fields': ('complete', 'paid', 'total')
        }),
    )
