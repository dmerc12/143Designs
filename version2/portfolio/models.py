from django.db import models

class Work(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=255)

    def __str__(self):
        return f"Name: {self.name} - Description: {self.description} \n"

class Review(models.Model):
    name = models.CharField(max_length=60)
    text = models.TextField(max_length=255)
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return f"Name: {self.name} - Text: {self.text} - Rating: {self.rating} \n"
