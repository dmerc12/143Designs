from .models import Category, Item, ItemImages
from django.utils.html import format_html
from django.contrib import admin

# Registers categories with admin site
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['custom_id', 'name', 'image_preview']
    
    # Displays a custom ID for the categories
    def custom_id(self, obj):
        return format_html(f'143DCAT{obj.id}')

    # Alters column header for custom ID function above 
    custom_id.short_description = 'Category ID'

# Inline for item images in admin site
class ItemImagesInline(admin.TabularInline):
    model = ItemImages
    extra = 1
    verbose_name = 'Images'
    verbose_name_plural = 'Images'

# Registers items with admin site
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImagesInline]
    list_display = ['custom_id', 'name', 'category', 'featured', 'sale', 'image_preview']
    list_filter = ['category', 'featured', 'sale']

    # Displays a custom ID for the items
    def custom_id(self, obj):
        return format_html(f'143DIT{obj.id}')
    
    # Alters column header for custom ID function above
    custom_id.short_description = 'Item ID'
