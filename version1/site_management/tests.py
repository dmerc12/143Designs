from .admin import MessageAdmin, TestimonialAdmin
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
        self.site = AdminSite()
        self.customer = Customer.objects.get(first_name='user', last_name='example')
        self.message = Message.objects.create(first_name='test', last_name='test', email='test@email.com', phone_number='+14052223333', title='test', message='message')
        self.testimonial = Testimonial.objects.create(customer=self.customer, review='test', featured=True)
        self.message_admin = MessageAdmin(Message, self.site)
        self.testimonial_admin = TestimonialAdmin(Testimonial, self.site)

    # Test admin message custom ID
    def test_message_admin_custom_id(self):
        self.assertEqual(self.message_admin.custom_id(self.message), f'143DMES{self.message.pk}')

    # Test admin testimonial custom ID
    def test_testimonial_admin_custom_id(self):
        self.assertEqual(self.testimonial_admin.custom_id(self.testimonial), f'143DTES{self.testimonial.pk}')

# Tests for site management views
class TestSiteManagementViews(TestCase):

    # Setup before each test
    def setUp(self):
        self.client = Client()

    ## Tests for home view
    # Test for home view rendering success
    def test_home_view_rendering_success(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        
    ## Tests for contact view
    # Test for contact view rendering success
    def test_contact_view_rendering_success(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertIsInstance(response.context['form'], ContactForm)
        
    # Test for contact view success
    def test_contact_view_success(self):
        data = {
            'first_name': 'first',
            'last_name': 'last',
            'email': 'test@email.com',
            'phone_number': '+12345678901',
            'title': 'title',
            'message': 'message'
        } 
        response = self.client.post(reverse('contact'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('store-home'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn("Your message has been successfully sent. We will be in contact soon! In the meantime, check out what's in stock in our store below!", messages)
   