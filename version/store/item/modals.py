from django.db import models
from django.urls import reverse

class Item(models.Model):
    objects = None
    name = models.CharField(max_length=60)

    def __str__(self):
        return f'ID: {self.pk} - Name: {self.name} \n'

    def get_absolute_url(self):
        return reverse('store')
