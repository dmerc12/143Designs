from .models import Category, Item, ItemImages
from django.utils.html import format_html
from django.contrib import admin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['custom_id', 'name', 'image_preview']
    
    def custom_id(self, obj):
        return format_html(f'143DCAT{obj.id}')
    
    custom_id.short_description = 'Category ID'

class ItemImagesInline(admin.TabularInline):
    model = ItemImages
    extra = 1
    verbose_name = 'Images'
    verbose_name_plural = 'Images'

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImagesInline]
    list_display = ['custom_id', 'name', 'category', 'status', 'image_preview']
    list_filter = ['category', 'status']
    
    def custom_id(self, obj):
        return format_html(f'143DIT{obj.id}')
    
    custom_id.short_description = 'Item ID'
