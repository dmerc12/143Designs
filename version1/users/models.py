from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models

class Admin(AbstractUser):
    pass

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
        self.save()

    def __str__(self):
        return self.username
    
Admin._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
Admin._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_user_permissions'

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
