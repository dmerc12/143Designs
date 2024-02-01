from .models import Product, Purchase, PurchaseProduct, PurchaseDesign, ProductSize, Design
from order_tracking.models import OrderProduct, OrderDesign
from django.utils.html import format_html
from django.db.models import Sum
from django.contrib import admin
from django.db import models
from django import forms

class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['custom_id', 'name', 'material', 'color', 'total_quantity_in_stock', 'display_sizes']
    list_filter = ['id', 'name', 'material', 'color']
    search_fields = ['name', 'material', 'color']
    inlines = [ProductSizeInline]

    def custom_id(self, obj):
        return f'143DPROD{obj.id}'
    
    custom_id.short_description = 'Product ID'

    def total_quantity_in_stock(self, obj):
        purchase_quantity = PurchaseProduct.objects.filter(product=obj).aggregate(Sum('quantity'))['quantity__sum'] or 0
        order_quantity = OrderProduct.objects.filter(item=obj, order__complete=True).aggregate(Sum('quantity'))['quantity__sum'] or 0
        total_quantity = purchase_quantity - order_quantity
        return total_quantity
    
    def display_sizes(self, obj):
        sizes_info = []
        product_sizes = ProductSize.objects.filter(product=obj)
        for size in product_sizes:
            purchase_quantity = PurchaseProduct.objects.filter(product_size=size).aggregate(Sum('quantity'))['quantity__sum'] or 0
            order_quantity = OrderProduct.objects.filter(size=size, order__complete=True).aggregate(Sum('quantity'))['quantity__sum'] or 0
            quantity_in_stock = purchase_quantity - order_quantity
            sizes_info.append(f'{size.size}: {quantity_in_stock}')
        return format_html("<br>".join(sizes_info))

    display_sizes.short_description = 'Stock'

@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    list_display = ['custom_id', 'name', 'description', 'image_preview', 'total_quantity_in_stock']
    search_fields = ['id', 'name', 'description']
    fields = ['name', 'description', 'image', 'image_preview', 'price', 'cost']
    readonly_fields = ['image_preview',]

    formfield_overrides = {
        models.ImageField: {'widget': forms.FileInput(attrs={'accept': 'image/*'})},
    }

    def total_quantity_in_stock(self, obj):
        purchase_quantity = PurchaseDesign.objects.filter(design=obj).aggregate(Sum('quantity'))['quantity__sum'] or 0
        order_quantity = OrderDesign.objects.filter(design=obj, order__complete=True).aggregate(Sum('quantity'))['quantity__sum'] or 0
        total_quantity = purchase_quantity - order_quantity
        return total_quantity

    def custom_id(self, obj):
        return f'143DDES{obj.id}'
    
    custom_id.short_description = 'Design ID'

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
