from .models import Product, Purchase, PurchaseProduct, Size
from order_tracking.models import OrderProduct
from django.utils.html import format_html
from django.db.models import Sum
from django.contrib import admin
from django import forms

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['item']

class SizeNameFilter(admin.SimpleListFilter):
    title = 'size'
    parameter_name = 'size_name'

    def lookups(self, request, model_admin):
        return Size.objects.values_list('name', 'name').distinct()

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(size__name=self.value())
        return queryset
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'material', 'color', 'size', 'price', 'cost', 'total_quantity_in_stock']
    list_filter = ['name', 'material', 'color', SizeNameFilter]
    search_fields = ['name', 'material', 'color', 'size__name', 'price', 'cost']
    form = ProductForm

    def total_quantity_in_stock(self, obj):
        purchase_quantity = PurchaseProduct.objects.filter(product=obj).aggregate(Sum('quantity'))['quantity__sum'] or 0
        order_quantity = OrderProduct.objects.filter(item=obj, order__complete=True).aggregate(Sum('quantity'))['quantity__sum'] or 0
        total_quantity = purchase_quantity - order_quantity
        return total_quantity

class PurchaseProductInline(admin.TabularInline):
    model = PurchaseProduct
    extra = 1

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['custom_id', 'supplier', 'notes', 'subtotal', 'total']
    list_filter = ['supplier__name']
    search_fields = ['id', 'supplier__name']
    inlines = [PurchaseProductInline]
    fieldsets = [
        (None, {
            'fields': ['supplier', 'notes'],
        }),
        ('Totals', {
            'fields': ['subtotal', 'total'],
        }),
    ]

    def custom_id(self, obj):
        return f'143DORD{obj.id}'

    custom_id.short_description = 'Purchase Number'
