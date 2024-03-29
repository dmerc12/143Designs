from phonenumber_field.modelfields import PhoneNumberField
from users.models import Customer
from django.db import models

# Messages for the contact page
class Message(models.Model):
    first_name = models.CharField(max_length=100, help_text='Enter your first name.')
    last_name = models.CharField(max_length=100, help_text='Enter your last name.')
    email = models.EmailField(max_length=250, help_text='Enter your email address.')
    phone_number = PhoneNumberField(help_text='Enter your phone number.')
    title = models.CharField(max_length=250, help_text='Enter a title for your message.')
    message = models.TextField(max_length=600, help_text='Enter your message.')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.title

# Testimonials to be displayed on the home page
class Testimonial(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, help_text='Choose the customer for the testimonial.')
    review = models.TextField(max_length=600, help_text='Enter the review for the testimonial.')
    featured = models.BooleanField(default=False, help_text='Indicate whether the testimonial should be featured on the home page.')

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        if self.featured:
            status = 'Featured'
        else:
            status = 'Not Featured'
        return f"{self.customer} - {status}"
