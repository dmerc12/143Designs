from django.contrib.auth.models import User, Group
from django.utils.html import format_html
from django.contrib import admin
from .models import Order

admin.site.unregister(Group)
admin.site.unregister(User)

class OrderProductInline(admin.TabularInline):
    model = Order.item.through
    extra = 1
    verbose_name = 'Item'
    verbose_name_plural = 'Items'

class OrderDesignInline(admin.TabularInline):
    model = Order.design.through
    extra = 1
    verbose_name = 'Design'
    verbose_name_plural = 'Designs'

@admin.action(description='Mark selected orders as complete')
def mark_complete(modeladmin, request, queryset):
    queryset.update(complete=True)

@admin.action(description='Mark selected orders as incomplete')
def mark_incomplete(modeladmin, request, queryset):
    queryset.update(complete=False)

@admin.action(description='Mark selected orders as paid')
def mark_paid(modeladmin, request, queryset):
    queryset.update(paid=True)

@admin.action(description='Mark selected orders as not paid')
def mark_unpaid(modeladmin, request, queryset):
    queryset.update(paid=False)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['custom_id_display', 'customer', 'short_description', 'total', 'complete', 'paid', 'last_modified', 'created']
    list_filter = ['created', 'last_modified', 'customer__first_name', 'customer__last_name', 'complete', 'paid', 'item']
    search_fields = ['created', 'last_modified', 'customer__first_name', 'customer__last_name', 'customer__email', 'customer__phone_number']
    actions = [mark_complete, mark_incomplete, mark_paid, mark_unpaid]
    date_hierarchy = 'created'
    inlines = [OrderProductInline, OrderDesignInline]
    fieldsets = (
        (None, {
            'fields': ('customer', 'short_description', 'description')
        }),
        ('Status', {
            'fields': ('complete', 'paid', 'total')
        }),
    )

    def custom_id_display(self, obj):
        return format_html(f'143DORD{obj.id}')
    
    custom_id_display.short_description = 'Order Number'
