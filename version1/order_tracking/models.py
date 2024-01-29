from inventory_tracking.models import Product
from users.models import Customer
from django.db import models

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, help_text='Choose a customer for the order.')
    short_description = models.CharField(max_length=150, help_text='Enter a short description for the order.')
    description = models.TextField(max_length=300, null=True, blank=True, help_text='Enter a description for the order.')
    total = models.DecimalField(max_digits=999999999, decimal_places=2, default=0, help_text='The total of the order will update with the items, or you can override it here.')
    complete = models.BooleanField(default=False, help_text='Indicate if the order is complete.')
    paid = models.BooleanField(default=False, help_text='Indicate if the order has been paid for.')
    item = models.ManyToManyField(Product, through="OrderProduct")
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def calculate_total(self):
        order_items = OrderProduct.objects.filter(order=self)
        total = sum(order_item.quantity * order_item.item.price for order_item in order_items)
        self.total = total
        self.save()

    def __str__(self):
        return f"143D{self.pk} - {self.short_description} - ${self.total}"

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
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
    