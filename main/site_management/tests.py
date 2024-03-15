from django.contrib.auth.models import User
from .models import Message, Testimonial
from django.test import TestCase
from .forms import ContactForm

# Tests for site management models
class TestSiteManagementModels(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', first_name='test', last_name='user', email='test@email.com', password='pass12345')

    ## Tests for messsage model
    ### Test for model string method
    def test_message_str(self):
        message = Message.objects.create(first_name='first', last_name='last', email='e@mail.com', phone_number='123123132541', title='title', message='message')
        self.assertEqual(str(message), f'{message.first_name} {message.last_name} - {message.title}')

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

    def setUp(self):
        pass

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
