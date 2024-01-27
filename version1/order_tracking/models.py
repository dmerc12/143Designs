from users.models import Customer
from django.db import models

class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50, help_text='Enter a name for the item. (i.e. Shirt, Hat, Sticker)')
    material = models.CharField(max_length=100, help_text='Enter the material of the item. (i.e. Cotton, Vinyl, Hemp)')
    color = models.CharField(max_length=60, help_text='Enter the color of the item. (i.e. Blue, Red,  Purple)')
    description = models.TextField(max_length=100, help_text='Enter a description for the item.')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, help_text='Choose the size of the item.')
    price = models.DecimalField(max_digits=999999999, decimal_places=2, help_text='Enter a price for the item. When added to an order, this will update the total.')

    def __str__(self):
        return f"{self.material} {self.name} - {self.size} - {self.price}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, help_text='Choose a customer for the order.')
    short_description = models.CharField(max_length=150, help_text='Enter a short description for the order.')
    description = models.TextField(max_length=300, help_text='Enter a description for the order.')
    total = models.DecimalField(max_digits=999999999, decimal_places=2, default=0, help_text='The total of the order will update with the items, or you can override it here.')
    complete = models.BooleanField(default=False, help_text='Indicate if the order is complete.')
    paid = models.BooleanField(default=False, help_text='Indicate if the order has been paid for.')
    item = models.ManyToManyField(Item, through="OrderItem")
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def calculate_total(self):
        order_items = OrderItem.objects.filter(order=self)
        total = sum(order_item.quantity * order_item.item.price for order_item in order_items)
        self.total = total
        self.save()

    def __str__(self):
        return f"143D{self.pk} - {self.short_description} - ${self.total}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.order.calculate_total()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.order.calculate_total()

    def __str__(self):
        return f"{self.order} - {self.quantity} of {self.item}"
    