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
    featured = models.BooleanField(default=True, help_text='Choose if you would like the item to be featured on the store home page.')
    sale = models.BooleanField(default=False, help_text='Indicate if you would like the item to be on sale.')

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return f'{self.category} - {self.name}'
    
    def image_preview(self):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(self.image.url))
    
    @property
    def min_price(self):
        sizes = self.product.get_product_sizes()
        min_price = min(size.price for size in sizes)
        total_min_price = min_price + self.design.price
        return total_min_price
    @property
    def max_price(self):
        sizes = self.product.get_product_sizes()
        max_price = max(size.price for size in sizes)
        total_max_price = max_price + self.design.price
        return total_max_price
    
class ItemImages(models.Model):
    images = models.ImageField(upload_to='store/item-images')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item Image'
        verbose_name_plural = 'Item Images'
