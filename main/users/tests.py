from .forms import LoginForm, RegisterForm, UpdateUserForm, ChangePasswordForm
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

# Tests for users forms
class TestUserForms(TestCase):

    def setUp(self):
        self.base = User.objects.create_user(username='username', password='testpass123', first_name='user', last_name='name', email='test@email.com')
        self.user = CustomUser.objects.create(user=self.base, role='admin', phone_number='phone number')

    ## Tests for login form
    ### Test for login form initialization
    def test_login_form_initialization(self):
        form = LoginForm()
        self.assertIn('username', form.fields.keys())
        self.assertIn('password', form.fields.keys())
        
    ### Test for login form validation with empty fields
    def test_login_form_validation_empty_fields(self):
        data = {'username': '', 'password': ''}
        form = LoginForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('password', form.errors)
        
    ### Test login form validation success
    def test_login_form_validation_success(self):
        data = {'username': self.base.username, 'password': self.base.password}
        form = LoginForm(data=data)
        self.assertTrue(form.is_valid())

    ## Tests for register form
    ### Test register form initialization
    def test_register_form_initialization(self):
        form = RegisterForm()
        self.assertIn('username', form.fields.keys())
        self.assertIn('email', form.fields.keys())
        self.assertIn('first_name', form.fields.keys())
        self.assertIn('last_name', form.fields.keys())
        self.assertIn('phone_number', form.fields.keys())
        self.assertIn('password1', form.fields.keys())
        self.assertIn('password2', form.fields.keys())

    ### Test register form validation with empty fields
    def test_register_form_validation_empty_fields(self):
        data = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'phone_number': '',
            'password1': '',
            'password2': ''
        }
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('phone_number', form.errors)
        self.assertIn('password1', form.errors)
        self.assertIn('password2', form.errors)

    ### Test register form validation with fields too long
    def test_register_form_validation_fields_too_long(self):
        data = {
            'username': 'test' * 50,
            'first_name': 'test' * 50,
            'last_name': 'test' * 50,
            'email': 'test' * 50 + '@email.com',
            'phone_number': '1' * 16,
            'password1': 'there is no max length for passwords',
            'password2': 'there is no max length for passwords'
        }
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('phone_number', form.errors)

    ### Test register form validation with invalid email
    def test_register_form_validation_invalid_email(self):
        data = {
            'username': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'incorrect format',
            'phone_number': '1-123-123-1234',
            'password1': 'there is no max length for passwords',
            'password2': 'there is no max length for passwords'
        }
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    ### Test register form validation with invalid password
    def test_register_form_validation_invalid_password(self):
        data = {
            'username': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@email.com',
            'phone_number': '1-123-123-1234',
            'password1': 'testtest',         
            'password2': 'testtest'
        }
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    ### Test register form validation with mismatching passwords
    def test_register_form_validation_mismatching_passwords(self):
        data = {
            'username': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@email.com',
            'phone_number': '1-123-123-1234',
            'password1': 'mismatching',         
            'password2': 'passwords'
        }
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    ### Test register form validation success
    def test_register_form_validation_successs(self):
        data = {
            'username': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@email.com',
            'phone_number': '1-123-123-1234',
            'password1': 'user12345',         
            'password2': 'user12345'
        }
        form = RegisterForm(data=data)
        self.assertTrue(form.is_valid())
        
    ## Tests for update user form
    ### Test update user form initialization
    def test_update_user_form_initialization(self):
        form = UpdateUserForm()
        self.assertIn('username', form.fields.keys())
        self.assertIn('first_name', form.fields.keys())
        self.assertIn('last_name', form.fields.keys())
        self.assertIn('email', form.fields.keys())
        self.assertIn('phone_number', form.fields.keys())

    ### Test update user form validation with empty fields
    def test_update_user_form_validation_empty_fields(self):
        data = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'phone_number': '',
        }
        form = UpdateUserForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('phone_number', form.errors)

    ### Test update user form validation with fields too long
    def test_update_user_form_validation_fields_too_long(self):
        data = {
            'username': 'test' * 50,
            'first_name': 'test' * 50,
            'last_name': 'test' * 50,
            'email': 'test' * 50 + '@email.com',
            'phone_number': '1' * 16,
        }
        form = UpdateUserForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('phone_number', form.errors)

    ### Test update user form validation with invalid email
    def test_update_user_form_validation_invalid_email(self):
        data = {
            'username': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'incorrect format',
            'phone_number': '1-123-123-1234'
        }
        form = UpdateUserForm(data=data)
        self.assertIn('email', form.errors)

    ### Test update user form validation success
    def test_update_user_form_validation_success(self):
        data = {
            'username': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@email.com',
            'phone_number': '1-123-123-1234'
        }
        form = UpdateUserForm(data=data)
        self.assertTrue(form.is_valid())
    
    ## Tests for change password form
    ### Test change password form initialization

    ### Test change password form validation with empty fields

    ### Test change password form validation with an invalid password

    ### Test change password form validation with mismatching passwords

    ### Test change password form validation success
