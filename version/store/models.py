from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=60)

class Order(models.Model):
    name = models.CharField(max_length=60)
    complete = models.BooleanField()
    paid = models.BooleanField()
    items = models.ManyToManyField(Item, through='OrderItem')
    description = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()