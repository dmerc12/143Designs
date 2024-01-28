from users.models import Supplier
from django.db.models import Sum
from django.db import models

class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50, help_text='Enter a name for the product. (i.e. Shirt, Hat, Sticker)')
    material = models.CharField(max_length=100, help_text='Enter the material of the product. (i.e. Cotton, Vinyl, Hemp)')
    color = models.CharField(max_length=60, help_text='Enter the color of the product. (i.e. Blue, Red,  Purple)')
    description = models.TextField(max_length=100, help_text='Enter a description for the product.')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, help_text='Choose the size of the product.')
    price = models.DecimalField(max_digits=999999999, decimal_places=2, help_text='Enter the price to sell the product for.')
    cost = models.DecimalField(max_digits=999999999, decimal_places=2, help_text='Enter the cost of the product.')

    def __str__(self):
        return f'{self.color} {self.material} {self.name} - ${self.price}'

class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    notes = models.TextField(max_length=150)
    products = models.ManyToManyField(Product, through='PurchaseProduct')
    subtotal = models.DecimalField(max_digits=999999999, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=999999999, decimal_places=2, default=0)

    def calculate_subtotal(self):
        purchase_items = PurchaseProduct.objects.filter(purchase=self)
        subtotal = sum(purchase_item.quantity * purchase_item.product.price for purchase_item in purchase_items)
        self.subtotal = subtotal
        self.save()
    
    def __str__(self):
        return f'143DORD{self.pk}'
    
class PurchaseProduct(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.purchase.calculate_subtotal()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.purchase.calculate_subtotal()

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
