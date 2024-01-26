from django.db import models
from users.models import Customer

item_size_choices = {
    'SM': 'Small',
    'MD': 'Medium',
    'LG': 'Large',
    'XL': 'XL',
    'XXL': 'XXL',
    'XXXL': 'XXXL'
}

class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    size = models.CharField(max_length=4, choices=item_size_choices)
    price = models.DecimalField(max_digits=999999999, decimal_places=2)
    material = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.material} {self.name} - {self.size} - {self.price}"
    
    get_verbose_name = 'Item'
    get_verbose_name_plural = 'Items'

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    total = models.DecimalField(max_digits=999999999, decimal_places=2, default=0)
    complete = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    item = models.ManyToManyField(Item, through="OrderItem")

    def __str__(self):
        return f"{self.pk} - {self.total} - {self.short_description}"
    
    get_verbose_name = 'Order'
    get_verbose_name_plural = 'Orders'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.order} - {self.quantity} of {self.item}"

