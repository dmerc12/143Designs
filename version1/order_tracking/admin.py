from django.contrib.auth.models import User, Group
from .models import Order, Item, Size, OrderItem
from django.contrib import admin
from django import forms

admin.site.unregister(Group)
admin.site.unregister(User)

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'

class ItemInline(admin.TabularInline):
    model = Order.item.through
    form = OrderItemForm
    extra = 1
    verbose_name = 'Item'
    verbose_name_plural = 'Items'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'short_description', 'total', 'complete', 'paid', 'last_modified', 'created']
    list_filter = ['created', 'last_modified', 'customer__first_name', 'customer__last_name', 'complete', 'paid', 'item']
    search_fields = ['created', 'last_modified', 'id', 'customer__first_name', 'customer__last_name', 'customer__email', 'customer__phone_number']
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
    list_display = ['name', 'material', 'color', 'size', 'price']
    list_filter = ['name', 'material', 'color', 'size']
