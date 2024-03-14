from django.contrib.auth.models import User
from .models import Message, Testimonial
from django.test import TestCase

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
