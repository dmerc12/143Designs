from django.db import models

class Work(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=255)

    def __str__(self):
        return f"Name: {self.name} - Description: {self.description} \n"

class Review(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    subject = models.CharField(max_length=100)
    text = models.TextField(max_length=255)
    rating = models.FloatField()
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name} - Subject: {self.subject} - Rating: {self.rating} \n"
