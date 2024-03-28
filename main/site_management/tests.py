from django.contrib.messages import get_messages
from users.models import CustomUser, Customer
from django.contrib.auth.models import User
from django.test import TestCase, Client
from .models import Message, Testimonial
from django.urls import reverse
from .forms import ContactForm

# Tests for site management models
class TestSiteManagementModels(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', first_name='test', last_name='user', email='test@email.com', password='pass12345')

    ## Tests for messsage model
    ### Test for model string method
    def test_message_str(self):
        customer = Customer.objects.create(first_name='first', last_name='last', email='e@mail.com', phone_number='1-222-333-4444')
        message = Message.objects.create(customer=customer, title='title', message='message')
        self.assertEqual(str(message), f'{customer.first_name} {customer.last_name} - {message.title}')

    ## Tests for testimonial model
    ### Test for model string method when featured
    def test_testimonial_str_featured(self):
        testimonial = Testimonial.objects.create(user=self.user, title='title', review='review', featured=True)
        self.assertEqual(str(testimonial), f'{testimonial.user.first_name} {testimonial.user.last_name} - {testimonial.title} - Featured')

    ### Test for model string method when not featured
    def test_testimonial_str_not_featured(self):
        testimonial = Testimonial.objects.create(user=self.user, title='title', review='review')
        self.assertEqual(str(testimonial), f'{testimonial.user.first_name} {testimonial.user.last_name} - {testimonial.title} - Not Featured')

# Tests for site management forms
class TestSiteManagementForms(TestCase):

    ## Tests for contact form
    ### Test contact form inialization
    def test_contact_form_inialization(self):
        form = ContactForm()
        self.assertIn('first_name', form.fields.keys())
        self.assertIn('last_name', form.fields.keys())
        self.assertIn('email', form.fields.keys())
        self.assertIn('phone_number', form.fields.keys())
        self.assertIn('title', form.fields.keys())
        self.assertIn('message', form.fields.keys())

    ### Test contact form validation with empty fields
    def test_contact_form_validation_empty_fields(self):
        data = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'phone_number': '',
            'title': '',
            'message': ''
        }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('phone_number', form.errors)
        self.assertIn('title', form.errors)
        self.assertIn('message', form.errors)

    ### Test contact form validation with fields too long
    def test_contact_form_validation_fields_too_long(self):
        data = {
            'first_name': 'success' * 150,
            'last_name': 'test' * 150,
            'email': 'success@test.com' * 150,
            'phone_number': '1-123-123-1234' * 15,
            'title': 'test title' * 250,
            'message': 'test message' * 600
        }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('phone_number', form.errors)
        self.assertIn('title', form.errors)
        self.assertIn('message', form.errors)

    ### Test contact form validation success
    def test_contact_form_validation_success(self):
        data = {
            'first_name': 'success',
            'last_name': 'test',
            'email': 'success@test.com',
            'phone_number': '1-123-123-1234',
            'title': 'test title',
            'message': 'test message'
        }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

# Tests for site management views
class TestSiteManagementViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.base = User.objects.create(username='test', password='test', first_name='first', last_name='last', email='firstlast@email.com')
        self.user = CustomUser.objects.create(user=self.base, phone_number='1-222-333-4444', role='admin')
        self.customer = Customer.objects.create(first_name='first', last_name='last', email='e@mail.com', phone_number='1-222-333-4444')
        self.message = Message.objects.create(customer=self.customer, title='title', message='message')

    ## Tests for home view
    ### Test home view rendering success
    def test_home_view_rendering_success(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    ## Tests for admin home view
    ### Test admin home view redirect
    def test_admin_home_view_redirect(self):
        response = self.client.get(reverse('admin'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('You must be a site admin access this page!', messages)

    ### Test admin home rendering success
    def test_admin_home_view_rendering_success(self):
        self.client.force_login(self.base)
        response = self.client.get(reverse('admin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_home.html')

    ## Tests for contact view
    ### Test contact view rendering success
    def test_contact_view_rendering_success(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'site_management/messages/contact.html')
        self.assertIsInstance(response.context['form'], ContactForm)

    ### Test contact view success
    def test_contact_view_success(self):
        data = {
            'first_name': 'success',
            'last_name': 'test',
            'email': 'success@test.com',
            'phone_number': '1-123-123-1234',
            'title': 'test title',
            'message': 'test message'
        }
        response = self.client.post(reverse('contact'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn(f"Your message has been successfully sent. We will be in contact soon!\nIn the meantime, check out our store!", messages)

    ## Tests for messages home view
    ### Test messages home view redirect
    def test_messages_home_view_redirect(self):
        response = self.client.get(reverse('messages-home'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('You must be a site admin access this page!', messages)

    ### Test messages home view rendering success
    def test_messages_home_view_rendering_success(self):
        self.client.force_login(self.base)
        response = self.client.get(reverse('messages-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'site_management/messages/home.html')

    ## Tests for delete message view
    ### Test delete message view redirect
    def test_delete_message_view_redirect(self):
        response = self.client.get(reverse('delete-message', args=[self.message.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('You must be a site admin access this page!', messages)

    ### Test delete message view rendering success
    def test_delete_message_view_rendering_success(self):
        self.client.force_login(self.base)
        response = self.client.get(reverse('delete-message', args=[self.message.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'site_management/messages/delete.html')

    ### Test delete message view success
    def test_delete_message_view_success(self):
        self.client.force_login(self.base)
        response = self.client.post(reverse('delete-message', args=[self.message.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('messages-home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('The message has been deleted!', messages)
