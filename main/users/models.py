from django.contrib.auth.models import User
from django.db import models

# Model for address for users
class Address(models.Model):
    name = models.CharField(max_length=250)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='addresses', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Model for users
class CustomUser(models.Model):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin')
    )
    role = models.CharField(max_length=5, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created  = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.user.username} - {self.role} - {self.active}'

# Model for customers
class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Model for suppliers
class Supplier(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=250)
    notes = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name
