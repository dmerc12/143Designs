from inventory_tracking.models import Product, Design
from django.utils.html import format_html
from django.db import models
from decimal import Decimal

# Categories for store items
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
    
# Store items combining the design and product from the inventory tracking app
class Item(models.Model):
    image = models.ImageField(upload_to='store/item')
    name = models.CharField(max_length=100, help_text='Enter a name for the item.')
    description = models.TextField(max_length=250, null=True, blank=True, help_text='Enter a description for the item.')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text='Choose a category for the item.')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text='Choose a product for the item.')
    design = models.ForeignKey(Design, on_delete=models.CASCADE, help_text='Choose a design for the item.')
    featured = models.BooleanField(default=True, help_text='Choose if you would like the item to be featured on the store home page.')
    sale = models.BooleanField(default=False, help_text='Indicate if you would like the item to be on sale.')
    sale_percentage = models.PositiveIntegerField(default=0, help_text='Input discount percentage as an integer.')

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return f'{self.category} - {self.name}'
    
    # Returns a preview of an image of the store item
    def image_preview(self):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(self.image.url))
    
    # Returns the min sale price of an item based on the sale percentage
    @property
    def sale_min_price(self):
        return (self.min_price - (self.min_price * Decimal(self.sale_percentage / 100))).quantize(Decimal('0.01'))

    # Returns the max sale price of an item based on the sale percentage
    @property
    def sale_max_price(self):
        return (self.max_price - (self.max_price * Decimal(self.sale_percentage / 100))).quantize(Decimal('0.01'))

    # Returns the minimum price of an item based on the sizes available
    @property
    def min_price(self):
        sizes = self.product.get_product_sizes()
        min_price = min(size.price for size in sizes)
        total_min_price = min_price + self.design.price
        return total_min_price
    
    # Returns the maximum price of an item based on the sizes available
    @property
    def max_price(self):
        sizes = self.product.get_product_sizes()
        max_price = max(size.price for size in sizes)
        total_max_price = max_price + self.design.price
        return total_max_price
    
# Images for a store item
class ItemImages(models.Model):
    images = models.ImageField(upload_to='store/item-images')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item Image'
        verbose_name_plural = 'Item Images'
