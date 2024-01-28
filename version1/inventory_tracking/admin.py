from .models import Product, Purchase, PurchaseProduct, Size
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
    form = ProductForm

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
