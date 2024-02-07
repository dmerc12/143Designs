from django.contrib.auth.models import User, Group
from django.utils.html import format_html
from django.contrib import admin
from .models import Order

# Unregisters default group and user models from admin site
admin.site.unregister(Group)
admin.site.unregister(User)

# Inline for items in an order in the admin site
class OrderItemInline(admin.TabularInline):
    model = Order.item.through
    extra = 1
    verbose_name = 'Item'
    verbose_name_plural = 'Items'

# Adds an action to mark selected orders as complete
@admin.action(description='Mark selected orders as complete')
def mark_complete(modeladmin, request, queryset):
    queryset.update(complete=True)

# Adds an action to mark selected orders as incomplete
@admin.action(description='Mark selected orders as incomplete')
def mark_incomplete(modeladmin, request, queryset):
    queryset.update(complete=False)

# Adds an action to mark selected orders as paid
@admin.action(description='Mark selected orders as paid')
def mark_paid(modeladmin, request, queryset):
    queryset.update(paid=True)

# Adds an action to mark selected orders as not paid
@admin.action(description='Mark selected orders as not paid')
def mark_unpaid(modeladmin, request, queryset):
    queryset.update(paid=False)

# Registers orders with the admin site
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['custom_id_display', 'customer', 'short_description', 'total', 'complete', 'paid', 'last_modified', 'created']
    list_filter = ['created', 'last_modified', 'customer__first_name', 'customer__last_name', 'complete', 'paid', 'item']
    search_fields = ['created', 'last_modified', 'customer__first_name', 'customer__last_name', 'customer__email', 'customer__phone_number']
    actions = [mark_complete, mark_incomplete, mark_paid, mark_unpaid]
    date_hierarchy = 'created'
    inlines = [OrderItemInline]
    fieldsets = (
        (None, {
            'fields': ('customer', 'short_description', 'description')
        }),
        ('Status', {
            'fields': ('complete', 'paid', 'total')
        }),
    )

    # Displays a custom ID for the orders
    def custom_id_display(self, obj):
        return format_html(f'143DORD{obj.id}')

    # Alters column header for custom ID function above
    custom_id_display.short_description = 'Order Number'
