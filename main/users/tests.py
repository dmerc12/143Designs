from .forms import LoginForm, RegisterForm, UpdateUserForm, ChangePasswordForm
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.test import TestCase, Client
from .models import Address, CustomUser
from django.urls import reverse

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
class TestUsersForms(TestCase):

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
    def test_change_password_form_initialization(self):
        form = ChangePasswordForm(user=self.base)
        self.assertIn('new_password1', form.fields.keys())
        self.assertIn('new_password2', form.fields.keys())

    ### Test change password form validation with empty fields
    def test_change_password_form_validation_empty_fields(self):
        data = {'new_password1': '', 'new_password2': ''}
        form = ChangePasswordForm(user=self.base, data=data)
        self.assertIn('new_password1', form.errors)
        self.assertIn('new_password2', form.errors)

    ### Test change password form validation with an invalid password
    def test_change_password_form_validation_invalid_password(self):
        data = {'new_password1': self.base.first_name, 'new_password2': self.base.first_name}
        form = ChangePasswordForm(user=self.base, data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('new_password2', form.errors)

    ### Test change password form validation with mismatching passwords
    def test_change_password_form_validation_mismatching_passwords(self):
        data = {'new_password1': 'mismatching', 'new_password2': 'passwords'}
        form = ChangePasswordForm(user=self.base, data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('new_password2', form.errors)

    ### Test change password form validation success
    def test_change_password_form_validation_success(self):
        data = {'new_password1': 'updatedpass123', 'new_password2': 'updatedpass123'}
        form = ChangePasswordForm(user=self.base, data=data)
        self.assertTrue(form.is_valid())

# Tests for users views
class TestUsersViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.base1 = User.objects.create_user(username='adminuser', password='pass12345', first_name='admin', last_name='admin', email='admin@email.com')
        self.user1 = CustomUser.objects.create(user=self.base1, role='admin', phone_number='1234567890')
        self.base2 = User.objects.create_user(username='username', password='pass12345', first_name='user', last_name='user', email='example@email.com')
        self.user2 = CustomUser.objects.create(user=self.base2, role='user', phone_number='1234567890')

    ## Tests for home view

    ## Tests for admin home view

    ## Tests for login view
    ### Test login view rendering success
    def test_login_view_rendering_success(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')
        self.assertIsInstance(response.context['form'], LoginForm)

    ### Test login view with incorrect credentials
    def test_login_view_incorrect_credentials(self):
        data = {'username': 'incorrect', 'password': 'credentials'}
        response = self.client.post(reverse('login'), data=data)
        self.assertEqual(response.status_code, 200)
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('Incorrect username or password, please try again!', messages)

    ### Test login view success with admin
    def test_login_view_admin_success(self):
        data = {'username': self.base1.username, 'password': 'pass12345'}
        response = self.client.post(reverse('login'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('admin-home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn(f'Welcome {self.base1.first_name} {self.base1.last_name}!', messages)

    ### Test login view success with user
    def test_login_view_user_success(self):
        data = {'username': self.base2.username, 'password': 'pass12345'}
        response = self.client.post(reverse('login'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn(f'Welcome {self.base2.first_name} {self.base2.last_name}!', messages)

    ## Tests for logout view
    ### Test logout view success
    def test_logout_view_success(self):
        self.client.force_login(self.base1)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('Goodbye!', messages)

    ## Tests for register view
    ### Test register view rendering success
    def test_register_view_rendering_success(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')
        self.assertIsInstance(response.context['form'], RegisterForm)

    ### Test register view success
    def test_register_view_success(self):
        data = {
            'username': 'testuser',
            'first_name': 'test',
            'last_name': 'user',
            'email': 'test@user.com',
            'phone_number': '1234567890',
            'password1': 'pass12345',
            'password2': 'pass12345'
        }
        response = self.client.post(reverse('register'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(User.objects.filter(username=data['username']).exists)
        self.assertTrue(CustomUser.objects.filter(user__username=data['username']).exists)
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn(f"Your account has been created and you have been logged in!\nWelcome {data['first_name']} {data['last_name']}!", messages)

    ## Tests for update user view
    ### Test update user vew redirect
    def test_update_user_view_redirect(self):
        response = self.client.get(reverse('update-user'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

    ### Test update user view rendering success
    def test_update_user_view_rendering_success(self):
        self.client.force_login(self.base1)
        response = self.client.get(reverse('update-user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/update.html')
        self.assertIsInstance(response.context['form'], UpdateUserForm)

    ### Test update user view success
    def test_update_user_view_success(self):
        self.client.force_login(self.base1)
        data = {
            'username': 'updated',
            'first_name': 'updated',
            'last_name': 'updated',
            'email': 'updated@email.com',
            'phone_number': '1-111-111-1111'
        }
        response = self.client.post(reverse('update-user'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(User.objects.filter(username=data['username']).exists())
        self.assertTrue(CustomUser.objects.filter(phone_number=data['phone_number']).exists())
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn(f"Your account has been successfully updated!", messages)

    ## Tests for change password view
