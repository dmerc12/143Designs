from django.db import models
from django.urls import reverse

from ..item.modals import Item

class Order(models.Model):
    name = models.CharField(max_length=60)
    complete = models.BooleanField()
    paid = models.BooleanField()
    items = models.ManyToManyField(Item, through='OrderItem')
    description = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f"ID: {self.pk} - Name: {self.name} - Complete: {self.complete} - Paid: {self.paid} - "
                f"Description: {self.description} - Created: {self.created} - Last Modified: {self.last_modified} \n")

    def get_absolute_url(self):
        return reverse('store-manage-orders')
