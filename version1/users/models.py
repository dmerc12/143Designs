from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

# Admin users for the admin site
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
    
# Add related_name attributes to avoid clashes with auth.User
Admin._meta.get_field('groups').remote_field.related_name = 'admin_user_groups'
Admin._meta.get_field('user_permissions').remote_field.related_name = 'admin_user_permissions'

# Automates creating admin when superuser is created
@receiver(post_save, sender=User)
def create_admin(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        admin_instance = Admin.objects.create(username=instance.username, email=instance.email)
        admin_instance.is_staff = True
        admin_instance.is_superuser = True
        admin_instance.save()

# Customers 
class Customer(models.Model):
    first_name = models.CharField(max_length=200, help_text='Please enter a first name for the customer')
    last_name = models.CharField(max_length=200, help_text='Please enter a last name for the customer')
    email = models.EmailField(max_length=250, help_text='Please enter an email for the customer')
    phone_number = models.CharField(max_length=20, help_text='Please enter a phone number for the customer')
    address1 = models.CharField(max_length=200, blank=True, help_text='Please enter an address for the customer')
    address2 = models.CharField(max_length=200, blank=True, help_text='Please enter an address for the customer')
    city = models.CharField(max_length=200, blank=True, help_text='Please enter a city for the customer')
    state = models.CharField(max_length=200, blank=True, help_text='Please enter a state for the customer')
    zipcode = models.CharField(max_length=200, blank=True, help_text='Please enter a zip code for the customer')
    country = models.CharField(max_length=200, blank=True, help_text='Please enter a country for the customer')
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

# Automate customer creation when registering with website
# Auto create customer when signing up with site
@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        if not Customer.objects.filter(user=instance).exists():
            customer = Customer(user=instance, first_name=instance.first_name, last_name=instance.last_name, email=instance.email)
            customer.save()

# Suppliers
class Supplier(models.Model):
    name = models.CharField(max_length=100, help_text='Enter the name of the supplier.')
    location = models.CharField(max_length=150, help_text='Enter the location of the supplier.')
    notes = models.TextField(max_length=300, null=True, blank=True, help_text='Enter any relevant notes about the supplier.')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        