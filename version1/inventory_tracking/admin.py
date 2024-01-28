from .models import Product, Purchase, PurchaseProduct, Size
from order_tracking.models import OrderProduct
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

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'material', 'color', 'size', 'price', 'cost', 'total_quantity_in_stock']
    list_filter = ['name', 'material', 'color', 'size']
    search_fields = ['name', 'material', 'color', 'size', 'price', 'cost']
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
    inlines = [PurchaseProductInline]
    fieldsets = [
        (None, {
            'fields': ['supplier', 'notes'],
        }),
        ('Totals', {
            'fields': ['subtotal', 'total'],
        }),
    ]
