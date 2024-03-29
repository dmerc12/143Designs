from .forms import LoginForm, RegisterForm, UpdateUserForm, ChangePasswordForm, AdminChangePasswordForm, CustomerForm
from .models import Address, CustomUser, Supplier, Customer
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.test import TestCase, Client
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
        self.assertEqual(str(user), f'{user.user.first_name} {user.user.last_name} - {user.user.username} - {user.role} - {user.active}')

    ## Tests for customer model
    ### Test for model string method
    def test_customer_str(self):
        customer = Customer.objects.create(first_name='first', last_name='last', email='first@email.com', phone_number='1-222-333-4444')
        self.assertEqual(str(customer), f'{customer.first_name} {customer.last_name}')

    ## Tests for supplier model
    ### Test for model string method
    def test_supplier_str(self):
        supplier = Supplier.objects.create(name='test', location='test')
        self.assertEqual(str(supplier), supplier.name)

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

    ## Tests for admin change password form
    ### Test admin change password form initialization
    def test_admin_change_password_form_initialization(self):
        form = ChangePasswordForm(user=self.base)
        self.assertIn('new_password1', form.fields.keys())
        self.assertIn('new_password2', form.fields.keys())

    ### Test admin change password form validation with empty fields
    def test_admin_change_password_form_validation_empty_fields(self):
        data = {'new_password1': '', 'new_password2': ''}
        form = ChangePasswordForm(user=self.base, data=data)
        self.assertIn('new_password1', form.errors)
        self.assertIn('new_password2', form.errors)

    ### Test admin change password form validation with an invalid password
    def test_admin_change_password_form_validation_invalid_password(self):
        data = {'new_password1': self.base.first_name, 'new_password2': self.base.first_name}
        form = ChangePasswordForm(user=self.base, data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('new_password2', form.errors)

    ### Test admin change password form validation with mismatching passwords
    def test_admin_change_password_form_validation_mismatching_passwords(self):
        data = {'new_password1': 'mismatching', 'new_password2': 'passwords'}
        form = ChangePasswordForm(user=self.base, data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('new_password2', form.errors)

    ### Test admin change password form validation success
    def test_admin_change_password_form_validation_success(self):
        data = {'new_password1': 'updatedpass123', 'new_password2': 'updatedpass123'}
        form = ChangePasswordForm(user=self.base, data=data)
        self.assertTrue(form.is_valid())

    ## Tests for customer form
    ### Test customer form initialization
    def test_customer_form_initialization(self):
        pass

    ### Test customer form validation with empty fields
    def test_customer_form_validataion_empty_fields(self):
        data = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'phone_number': '',
        }
        form = CustomerForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('phone_number', form.errors)

    ### Test customer form validation with fields too long
    def test_customer_form_validation_fields_too_long(self):
        data = {
            'username': 't' * 160,
            'first_name': 't' * 160,
            'last_name': 't' * 160,
            'email': (('test' * 150) + '@email.com'),
            'phone_number': '1' * 17,
        }
        form = CustomerForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('phone_number', form.errors)

    ### Test customer form validation with invalid email
    def test_customer_form_validation_invalid_email(self):
        data = {
            'username': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'incorrect format',
            'phone_number': '1-123-123-1234',
        }
        form = CustomerForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    ### Test customer form validation success
    def test_customer_form_validation_success(self):
        data = {
            'username': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@email.com',
            'phone_number': '1-123-123-1234',
        }
        form = CustomerForm(data=data)
        self.assertTrue(form.is_valid())

# Tests for users views
class TestUsersViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.base1 = User.objects.create_user(username='adminuser', password='pass12345', first_name='admin', last_name='admin', email='admin@email.com')
        self.user1 = CustomUser.objects.create(user=self.base1, role='admin', phone_number='1234567890')
        self.base2 = User.objects.create_user(username='username', password='pass12345', first_name='user', last_name='user', email='example@email.com')
        self.user2 = CustomUser.objects.create(user=self.base2, role='user', phone_number='1234567890')
        self.base3 = User.objects.create_user(username='anotheradmin', password='pass12345', first_name='user', last_name='user', email='example@email.com')
        self.user3 = CustomUser.objects.create(user=self.base3, role='admin', phone_number='1234567890')
        self.customer = Customer.objects.create(first_name='first', last_name='last', email='email@email.com', phone_number='1-222-333-4444')

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
        self.assertRedirects(response, reverse('admin'))
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
        self.assertTemplateUsed(response, 'users/users/register.html')
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

    ## Tests for register admin view
    ### Test register admin view redirect
    def test_register_admin_view_redirect(self):
        self.client.force_login(self.base2)
        response = self.client.get(reverse('register-admin'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('You must be a site admin access this page!', messages)

    ### Test register admin view rendering success
    def test_register_admin_view_rendering_success(self):
        self.client.force_login(self.base1)
        response = self.client.get(reverse('register-admin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/admin/register.html')
        self.assertIsInstance(response.context['form'], RegisterForm)

    ### Test register admin view success
    def test_register_admin_view_success(self):
        self.client.force_login(self.base1)
        data = {
            'username': 'testuser',
            'first_name': 'test',
            'last_name': 'user',
            'email': 'test@user.com',
            'phone_number': '1234567890',
            'password1': 'pass12345',
            'password2': 'pass12345'
        }
        response = self.client.post(reverse('register-admin'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('admin-home'))
        self.assertTrue(User.objects.filter(username=data['username']).exists)
        self.assertTrue(CustomUser.objects.filter(user__username=data['username']).exists)
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn(f"Admin account {data['first_name']} {data['last_name']} has been created and they can now use their credentials to login!", messages)

    ## Tests for admin home
    ### Test for admin home redirect
    def test_admin_home_redirect(self):
        response = self.client.get(reverse('admin-home'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('You must be a site admin access this page!', messages)

    ### Test for admin home rendering success
    def test_admin_home_rendering_success(self):
        self.client.force_login(self.base1)
        response = self.client.get(reverse('admin-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/admin/home.html')

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
        self.assertTemplateUsed(response, 'users/users/update.html')
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
    ### Test change password view redirect
    def test_change_password_redirect(self):
        response = self.client.get(reverse('change-password'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

    ### Test change password view rendering success
    def test_change_password_view_rendering_success(self):
        self.client.force_login(self.base1)
        response = self.client.get(reverse('change-password'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users/change_password.html')
        self.assertIsInstance(response.context['form'], ChangePasswordForm)

    ### Test change password view success
    def test_change_password_success(self):
        self.client.force_login(self.base1)
        data = {
            'new_password1': 'new12345',
            'new_password2': 'new12345'
        }
        response = self.client.post(reverse('change-password'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn(f"Your password has been successfully changed!", messages)

    ## Tests for delete user view
    ### Test delete user view redirect
    def test_delete_user_redirect(self):
        response = self.client.get(reverse('delete-user'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

    ### Test delete user view rendering success
    def test_delete_user_view_rendering_success(self):
        self.client.force_login(self.base1)
        response = self.client.get(reverse('delete-user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users/delete.html')

    ### Test delete user view success
    def test_delete_user_success(self):
        self.client.force_login(self.base2)
        response = self.client.post(reverse('delete-user'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn(f"Your profile has been successfully deleted, goodbye!", messages)

    ## Tests for activate admin view
    ### Test activate admin view redirect
    def test_activate_admin_view_redirect(self):
        response = self.client.get(reverse('activate-admin', args=[self.user1.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('You must be a site admin access this page!', messages)

    ### Test activate admin view rendering success
    def test_activate_admin_view_rendering_success(self):
        self.client.force_login(self.base3)
        response = self.client.get(reverse('activate-admin', args=[self.user1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/admin/activate.html')

    ### Test activate admin view success
    def test_activate_admin_view_success(self):
        self.client.force_login(self.base3)
        response = self.client.post(reverse('activate-admin', args=[self.user1.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('admin-home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn(f'The profile for {self.base1.first_name} {self.base1.last_name} has been activated!', messages)

    ## Tests for deactivate admin view
    ### Test deactivate admin view redirect
    def test_deactivate_admin_view_redirect(self):
        response = self.client.get(reverse('deactivate-admin', args=[self.user1.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('You must be a site admin access this page!', messages)

    ### Test deactivate admin view rendering success
    def test_deactivate_admin_view_rendering_success(self):
        self.client.force_login(self.base3)
        response = self.client.get(reverse('deactivate-admin', args=[self.user1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/admin/deactivate.html')

    ### Test deactivate admin view success
    def test_deactivate_admin_view_success(self):
        self.client.force_login(self.base3)
        response = self.client.post(reverse('deactivate-admin', args=[self.user1.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('admin-home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn(f'The profile for {self.base1.first_name} {self.base1.last_name} has been deactivated!', messages)

    ## Tests for admin reset password view
    ### Test admin reset password view redirect
    def test_admin_reset_password_view_redirect(self):
        response = self.client.get(reverse('admin-reset-password', args=[self.user1.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('You must be a site admin access this page!', messages)

    ### Test admin reset password view rendering success
    def test_admin_reset_password_view_rendering_success(self):
        self.client.force_login(self.base3)
        response = self.client.get(reverse('admin-reset-password', args=[self.user1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/admin/reset_password.html')
        self.assertIsInstance(response.context['form'], AdminChangePasswordForm)

    ### Test admin reset password view success
    def test_admin_reset_password_view_success(self):
        data = {
            'new_password1': 'resetpassword',
            'new_password2': 'resetpassword'
        }
        self.client.force_login(self.base3)
        response = self.client.post(reverse('admin-reset-password', args=[self.user1.pk]), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('admin-home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn(f'The password for {self.base1.first_name} {self.base1.last_name} has been reset!', messages)

    ## Tests for customer home view
    ### Test customer home view redirect
    def test_customer_home_view_redirect(self):
        response = self.client.get(reverse('customer-home'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('You must be a site admin access this page!', messages)

    ### Test customer home view rendering success
    def test_customer_home_view_rendering_success(self):
        self.client.force_login(self.base3)
        response = self.client.get(reverse('customer-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/customer/home.html')

    ## Tests for create customer view
    ### Test create customer view redirect
    def test_create_customer_view_redirect(self):
        response = self.client.get(reverse('create-customer'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('You must be a site admin access this page!', messages)

    ### Test create customer view rendering success
    def test_create_customer_view_rendering_success(self):
        self.client.force_login(self.base3)
        response = self.client.get(reverse('create-customer'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/customer/create.html')
        self.assertIsInstance(response.context['form'], CustomerForm)

    ### Test create customer view success
    def test_create_customer_view_success(self):
        data = {
            'first_name': 'first',
            'last_name': 'last',
            'email': 'test@email.com',
            'phone_number': '1-222-333-4444'
        }
        self.client.force_login(self.base3)
        response = self.client.post(reverse('create-customer'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('customer-home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('Customer successfully created!', messages)

    ## Tests for edit customer view
    ### Test edit customer view redirect
    def test_edit_customer_view_redirect(self):
        response = self.client.get(reverse('edit-customer', args=[self.customer.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('You must be a site admin access this page!', messages)

    ### Test edit customer view rendering success
    def test_edit_customer_view_rendering_success(self):
        self.client.force_login(self.base3)
        response = self.client.get(reverse('edit-customer', args=[self.customer.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/customer/edit.html')
        self.assertIsInstance(response.context['form'], CustomerForm)

    ### Test edit customer view success
    def test_edit_customer_view_success(self):
        data = {
            'first_name': 'first',
            'last_name': 'last',
            'email': 'test@email.com',
            'phone_number': '1-222-333-4444'
        }
        self.client.force_login(self.base3)
        response = self.client.post(reverse('edit-customer', args=[self.customer.pk]), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('customer-home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('Customer successfully updated!', messages)

    ## Tests for delete customer view
    ### Test delete customer view redirect
    def test_delete_customer_view_redirect(self):
        response = self.client.get(reverse('delete-customer', args=[self.customer.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('You must be a site admin access this page!', messages)

    ### Test delete customer view rendering success
    def test_delete_customer_view_rendering_success(self):
        self.client.force_login(self.base3)
        response = self.client.get(reverse('delete-customer', args=[self.customer.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/customer/delete.html')

    ### Test delete customer view success
    def test_delete_customer_view_success(self):
        self.client.force_login(self.base3)
        response = self.client.post(reverse('delete-customer', args=[self.customer.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('customer-home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('Customer successfully deleted!', messages)
