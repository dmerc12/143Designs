from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=255)
    complete = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=99999999999999, decimal_places=2, default=0)

    def __str__(self):
        return "Order - " + str(self.pk)

class Item(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return str(self.name)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return "Order - " + str(self.order.pk) + " - Item - " + str(self.item.name) + " - Quantity - " + str(self.quantity)
