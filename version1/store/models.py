from inventory_tracking.models import Product, Design
from django.utils.html import format_html
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, help_text='Enter a name for the category.')
    image = models.ImageField(upload_to=f'store/category/', help_text='Upload an image for the category.')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    def image_preview(self):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(self.image.url))
    
class Item(models.Model):
    image = models.ImageField(upload_to='store/item')
    name = models.CharField(max_length=100, help_text='Enter a name for the item.')
    description = models.TextField(max_length=250, null=True, blank=True, help_text='Enter a description for the item.')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text='Choose a category for the item.')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text='Choose a product for the item.')
    design = models.ForeignKey(Design, on_delete=models.CASCADE, help_text='Choose a design for the item.')
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return f'{self.category} - {self.name}'
    
    def image_preview(self):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(self.image.url))
    
class ItemImages(models.Model):
    images = models.ImageField(upload_to='store/item-images')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item Image'
        verbose_name_plural = 'Item Images'
