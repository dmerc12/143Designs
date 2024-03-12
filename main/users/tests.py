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
        pass

    ### Test register form validation with empty fields
    def test_register_form_validation_empty_fields(self):
        pass

    ### Test register form validation with fields too long
    def test_register_form_validation_fields_too_long(self):
        pass

    ### Test register form validation with invalid email
    def test_register_form_validation_invalid_email(self):
        pass

    ### Test register form validation with invalid password
    def test_register_form_validation_invalid_password(self):
        pass

    ### Test register form validation with mismatching passwords
    def test_register_form_validation_mismatching_passwords(self):
        pass

    ### Test register form validation success
    def test_register_form_validation_successs(self):
        pass
        
    ## Tests for update user form
    
    ## Tests for change password form
