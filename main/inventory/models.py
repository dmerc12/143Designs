from django.utils.html import format_html
from users.models import Supplier
from django.db import models
from itertools import chain

# Model for physical product
class Product(models.Model):
    name = models.CharField(max_length=150)
    material = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    description = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f'{self.color} {self.material} {self.name}'

    def get_product_sizes(self):
        return ProductSize.objects.filter(product=self)

# Model for sizes of physical product
class ProductSize(models.Model):
    size = models.CharField(max_length=150)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.size} ${self.price} - {self.product.__str__()}'

# Model for designs that can be used with product
class Design(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=250, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to='inventory/designs')

    def __str__(self):
        return f'{self.name} - ${self.price}'

    def image_preview(self):
        return format_html(f'<img src="{self.image.url}" style="max-width:200px; max-height: 200px"/>')
  
# Model for purchases of product and/or designs 
class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    notes = models.TextField(max_length=250, null=True, blank=True)
    products = models.ManyToManyField(Product, through='PurchaseProduct')
    designs = models.ManyToManyField(Design, through='PurchaseDesign')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'143DPUR{self.pk}'

    def calculate_subtotal(self):
        purchase_products = PurchaseProduct.objects.filter(purchase=self)
        purchase_designs = PurchaseDesign.objects.filter(purchase=self)
        purchase_items = list(chain(purchase_products, purchase_designs))
        subtotal = sum(purchase_item.quantity * (purchase_item.product_size.cost if isinstance(purchase_item, PurchaseProduct) else purchase_item.design.cost)for purchase_item in purchase_items)
        self.subtotal = subtotal
        self.save()
    
# Model for purchase products
class PurchaseProduct(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.purchase.calculate_subtotal()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.purchase.calculate_subtotal()

# Model for purchase designs
class PurchaseDesign(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    design = models.ForeignKey(Design, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.purchase.calculate_subtotal()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.purchase.calculate_subtotal()
