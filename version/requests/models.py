from django.db import models

class Request(models.Model):
    first_name = models.CharField(max_length=36)
    last_name = models.CharField(max_length=36)
    company_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    phone = models.CharField(max_length=15)
    message = models.TextField(max_length=255)
    complete = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"Name: {self.first_name} {self.last_name} - Company: {self.company_name} - Email: {self.email} - "
                f"Phone: {self.phone} - Message: {self.message} - Complete: {self.complete} - "
                f"Created: {self.created} \n")
