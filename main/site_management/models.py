from django.contrib.auth.models import User
from django.db import models

# Model for messages
class Message(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=15)
    title = models.CharField(max_length=250)
    message = models.TextField(max_length=600)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.title}'

# Model for testimonials
class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    review = models.TextField(max_length=600)
    featured = models.BooleanField(default=False)

    def __str__(self):
        if self.featured:
            status = 'Featured'
        else:
            status = 'Not Featured'
        return f'{self.user.first_name} {self.user.last_name} - {self.title} - {status}'
