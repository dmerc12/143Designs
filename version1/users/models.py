from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.db import models

class Admin(AbstractUser):
    pass

    def save(self, *args, **kwargs):
        self.is_staff = True
        self.is_superuser = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'
    
Admin._meta.get_field('groups').remote_field.related_name = 'admin_user_groups'
Admin._meta.get_field('user_permissions').remote_field.related_name = 'admin_user_user_permissions'

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'