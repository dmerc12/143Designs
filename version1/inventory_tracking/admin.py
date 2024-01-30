from .models import Product, Purchase, PurchaseProduct, PurchaseDesign, Size, Design
from order_tracking.models import OrderProduct
from django.utils.html import format_html
from django.db.models import Sum
from django.contrib import admin
from django.db import models
from django import forms

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['custom_id', 'name']
    search_fields = ['id', 'name']

    def custom_id(self, obj):
        return f'143DS{obj.id}'
    
    custom_id.short_description = 'Size ID'

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
    list_display = ['custom_id', 'name', 'material', 'color', 'size', 'price', 'cost', 'total_quantity_in_stock']
    list_filter = ['id', 'name', 'material', 'color', SizeNameFilter]
    search_fields = ['name', 'material', 'color', 'size__name', 'price', 'cost']

    def custom_id(self, obj):
        return f'143DPROD{obj.id}'
    
    custom_id.short_description = 'Product ID'

    def total_quantity_in_stock(self, obj):
        purchase_quantity = PurchaseProduct.objects.filter(product=obj).aggregate(Sum('quantity'))['quantity__sum'] or 0
        order_quantity = OrderProduct.objects.filter(item=obj, order__complete=True).aggregate(Sum('quantity'))['quantity__sum'] or 0
        total_quantity = purchase_quantity - order_quantity
        return total_quantity
    
@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    list_display = ['custom_id', 'name', 'description', 'image_preview']
    search_fields = ['id', 'name', 'description']
    fields = ['name', 'description', 'image', 'image_preview', 'price', 'cost']
    readonly_fields = ['image_preview',]

    formfield_overrides = {
        models.ImageField: {'widget': forms.FileInput(attrs={'accept': 'image/*'})},
    }

    def custom_id(self, obj):
        return f'143DDES{obj.id}'
    
    custom_id.short_description = 'Design ID'

    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    image_preview.short_description = "Design Preview"

class PurchaseProductInline(admin.TabularInline):
    model = PurchaseProduct
    extra = 1
    verbose_name_plural = 'Items'

class PurchaseDesignInline(admin.TabularInline):
    model = PurchaseDesign
    extra = 1
    verbose_name_plural = 'Designs'

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['custom_id', 'supplier', 'notes', 'subtotal', 'total']
    list_filter = ['supplier__name']
    search_fields = ['id', 'supplier__name']
    inlines = [PurchaseProductInline, PurchaseDesignInline]
    fieldsets = [
        (None, {
            'fields': ['supplier', 'notes'],
        }),
        ('Totals', {
            'fields': ['subtotal', 'total'],
        }),
    ]

    def custom_id(self, obj):
        return f'143DPUR{obj.id}'

    custom_id.short_description = 'Purchase Number'
