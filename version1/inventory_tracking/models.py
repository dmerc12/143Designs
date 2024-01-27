from..order_tracking.models import Size, Item
from ..users.models import Admin
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, help_text='Enter a name for the product. (i.e. Shirt, Hat, Sticker)')
    material = models.CharField(max_legth=100, help_text='Enter the material of the product. (i.e. Cotton, Vinyl, Hemp)')
    description = models.TextField(max_length=100, help_text='Enter a description for the product.')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, help_text='Choose the size of the product.')
    price = models.DecimalField(max_digits=999999999, decimal_places=2, help_text='Enter the price to sell the product for.')
    quantity = models.IntegerField(default=0, help_text='Specify the quantity of the product.')
    paid_for = models.DecimalField(max_digits=999999999, decimal_places=2, help_text='Enter the price paid for the product.')
    item = models.OneToOneField(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    user = models.ForeignKey(Admin, on_delete=models.CASCADE, help_text='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text='')
    quantity = models.PositiveIntegerField(help_text='')
    total = models.DecimalField(max_digits=999999999, decimal_places=2, help_text='')
    
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
