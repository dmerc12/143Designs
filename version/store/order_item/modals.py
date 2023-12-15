from django.db import models
from django.urls import reverse

from ..order.modals import Order
from ..item.modals import Item


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"ID: {self.pk} - Order Name: {self.order.name} - Item: {self.item.name} - Quantity: {self.quantity} \n"

    def get_absolute_url(self):
        return reverse('store-manage-order-item')
