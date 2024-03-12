from django.contrib.auth.models import User
from .models import Address, CustomUser
from django.test import TestCase

# Tests for users models
class TestUsersModels(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='username', password='password', first_name='user', last_name='name')

    ## Tests for address model
    ### Test for model string method
    def test_address_str(self):
        address = Address.objects.create(name='', address1='address1', address2='address2', city='city', state='state', zipcode='zipcode', country='country', user=self.user)
        self.assertEqual(str(address), f'{address.name}')

    ## Tests for custom user model
    ### Test for model string method
    def test_user_str(self):
        user = CustomUser.objects.create(user=self.user, role='admin', phone_number='phone number')
        self.assertEqual(str(user), f'{user.user.first_name} {user.user.last_name} - {user.user.username} - {user.role}')
