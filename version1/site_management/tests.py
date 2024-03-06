from django.contrib.admin.sites import AdminSite
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from .models import *
from .forms import *

# Tests for site management models
class TestSiteManagementModels(TestCase):

    # Setup before each test
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', email='user@example.com', password='testpassword', first_name='user', last_name='example')
        self.message = Message.objects.create(first_name='test', last_name='test', email='test@email.com', phone_number='+14052223333', title='test', message='message')
        self.customer = Customer.objects.get(user=self.user)
        self.testimonial1 = Testimonial.objects.create(customer=self.customer, review='test', featured=True)
        self.testimonial2 = Testimonial.objects.create(customer=self.customer, review='test', featured=False)

    # Test for message model string method
    def test_message_model_str_method(self):
        self.assertEqual(str(self.message), f'{self.message.title}')
        
    # test for featured testimonial model string method
    def test_featured_testimonial_model_str_method(self):
        self.assertEqual(str(self.testimonial1), f'{self.testimonial1.customer} - Featured')
        
    # test for not featured testimonial model string method
    def test_not_featured_testimonial_model_str_method(self):
        self.assertEqual(str(self.testimonial2), f'{self.testimonial2.customer} - Not Featured')
        
# Tests for site management admin
class TestSiteManagementAdmin(TestCase):

    # Setup before each test
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', email='user@example.com', password='testpassword', first_name='user', last_name='example')
        self.message = Message.objects.create(first_name='test', last_name='test', email='test@email.com', phone_number='+14052223333', title='test', message='message')
        self.customer = Customer.objects.get(user=self.user)
        self.testimonial1 = Testimonial.objects.create(customer=self.customer, review='test', featured=True)
        self.testimonial2 = Testimonial.objects.create(customer=self.customer, review='test', featured=False)
