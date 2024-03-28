from django.contrib.auth.models import User
from users.models import Customer
from django.db import models

# Model for messages
class Message(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    message = models.TextField(max_length=600)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer.first_name} {self.customer.last_name} - {self.title}'

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
