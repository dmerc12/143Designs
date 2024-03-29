from django.utils.html import format_html
from users.models import Supplier
from django.db import models
from itertools import chain

# Product to be combined with designs to create store items
class Product(models.Model):
    name = models.CharField(max_length=50, help_text='Enter a name for the product. (i.e. Shirt, Hat, Sticker)')
    material = models.CharField(max_length=100, help_text='Enter the material of the product. (i.e. Cotton, Vinyl, Hemp)')
    color = models.CharField(max_length=60, help_text='Enter the color of the product. (i.e. Blue, Red,  Purple)')
    description = models.TextField(max_length=100, null=True, blank=True, help_text='Enter a description for the product.')

    def __str__(self):
        return f'{self.color} {self.material} {self.name}'
    
    # Returns a list of the sizes of a product
    def get_product_sizes(self):
        return ProductSize.objects.filter(product=self)

# Sizes for the product above
class ProductSize(models.Model):
    size = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text='Enter the cost of the product.')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text='Enter the price to sell the product for.')

    def __str__(self):
        return f'{self.size} ${self.price} - {self.product.__str__()}'
    
# Designs to be combined with product to create store items
class Design(models.Model):
    name = models.CharField(max_length=50, help_text='Enter a name for the design.')
    description = models.TextField(max_length=150, null=True, blank=True, help_text='Enter a description or notes for the design.')
    image = models.ImageField(upload_to='inventory-tracking/designs/', help_text='Upload an image for the design.')
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text='Enter the cost of the product.')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text='Enter the price to sell the product for.')

    def __str__(self):
        return f'{self.name} - ${self.price}'
    
    # Returns a preview of an image of the design
    def image_preview(self):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(self.image.url))

# Purchases to track inventory of designs and products to be combined into store items
class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    notes = models.TextField(max_length=150, null=True, blank=True)
    products = models.ManyToManyField(Product, through='PurchaseProduct')
    designs = models.ManyToManyField(Design, through='PurchaseDesign')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Calculates the subtotal for a purchase
    def calculate_subtotal(self):
        purchase_products = PurchaseProduct.objects.filter(purchase=self)
        purchase_designs = PurchaseDesign.objects.filter(purchase=self)
        purchase_items = list(chain(purchase_products, purchase_designs))
        subtotal = sum(purchase_item.quantity * (purchase_item.product_size.cost if isinstance(purchase_item, PurchaseProduct) else purchase_item.design.cost)for purchase_item in purchase_items)
        self.subtotal = subtotal
        self.save()
    
    def __str__(self):
        return f'143DPUR{self.pk}'
    
# Products in a purchase to keep track of the inventory
class PurchaseProduct(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.purchase.calculate_subtotal()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.purchase.calculate_subtotal()

# Designs in the purchase to keep track of inventory
class PurchaseDesign(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    design = models.ForeignKey(Design, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.purchase.calculate_subtotal()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.purchase.calculate_subtotal()
