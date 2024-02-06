from inventory_tracking.models import Design, ProductSize
from users.models import Customer
from store.models import Item
from django.db import models
from itertools import chain

# Orders for the custom order tracking and the store apps
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, help_text='Choose a customer for the order.')
    short_description = models.CharField(max_length=150, help_text='Enter a short description for the order.')
    description = models.TextField(max_length=300, null=True, blank=True, help_text='Enter a description for the order.')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text='The total of the order will update with the items, or you can override it here.')
    discount = models.DecimalField(default=0, max_digits=10, decimal_places=2, help_text='Enter the amount off for the discount.')
    complete = models.BooleanField(default=False, help_text='Indicate if the order is complete.')
    paid = models.BooleanField(default=False, help_text='Indicate if the order has been paid for.')
    shipped = models.BooleanField(default=False, help_text='Indicate if the order has been shipped.')
    item = models.ManyToManyField(Item, through="OrderItem")
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    # Calculates total for an order
    def calculate_total(self):
        order_items = OrderItem.objects.filter(order=self)
        subtotal = sum((order_item.size.price + order_item.item.design.price) for order_item in order_items)
        total = subtotal - self.discount
        self.total = total
        self.save()

    def __str__(self):
        return f'143D{self.pk}'

# Items in an order
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

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
    