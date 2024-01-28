from order_tracking.models import Size, Item
from users.models import Admin, Supplier
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, help_text='Enter a name for the product. (i.e. Shirt, Hat, Sticker)')
    material = models.CharField(max_length=100, help_text='Enter the material of the product. (i.e. Cotton, Vinyl, Hemp)')
    color = models.CharField(max_length=60, help_text='Enter the color of the product. (i.e. Blue, Red,  Purple)')
    description = models.TextField(max_length=100, help_text='Enter a description for the product.')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, help_text='Choose the size of the product.')
    price = models.DecimalField(max_digits=999999999, decimal_places=2, help_text='Enter the price to sell the product for.')
    cost = models.DecimalField(max_digits=999999999, decimal_places=2, help_text='Enter the cost of the product.')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        item, created = Item.objects.get_or_create(
            name = self.name,
            material = self.material,
            color = self.color,
            description = self.description,
            size = self.size,
            price = self.price
        )
        if created:
            self.item = item
        super().save(*args, **kwargs)

class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    notes = models.TextField(max_length=150)
    products = models.ManyToManyField(Product, through='PurchaseProduct')
    subtotal = models.DecimalField(max_digits=999999999, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=999999999, decimal_places=2, default=0)
    
    def __str__(self):
        return f'Purchase - {self.pk}'
    
class PurchaseProduct(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
