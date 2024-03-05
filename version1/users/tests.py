from django.contrib.admin.sites import AdminSite
from .admin import CustomerAdmin, SupplierAdmin
from django.contrib.auth.models import User
from django.test import TestCase
from .models import *
from .forms import *

# Tests for users models
class TestUsersModels(TestCase):

    # Setup before each test
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', email='user@example.com', password='testpassword', first_name='user', last_name='example')
        self.superuser = User.objects.create_superuser(username='test_superuser', email='superuser@example.com', password='testpassword')
        self.admin = Admin(username='testadmin', email='testadmin@example.com')
        self.customer = Customer(first_name='John', last_name='Doe', email='john.doe@example.com', phone_number='+12156783467')
        self.supplier = Supplier(name='ABC Supplier', location='Somewhere', notes='test supplier notes')

    # Test for admin save method
    def test_admin_save(self):
        self.admin.save()
        self.assertTrue(self.admin.is_staff)
        self.assertTrue(self.admin.is_superuser)

    # Test for admin string method
    def test_admin_str(self):
        self.assertEqual(str(self.admin), 'testadmin')

    # Test for create admin function
    def test_create_admin_function(self):
        admin_created = Admin.objects.filter(username=self.superuser.username).exists()
        self.assertTrue(admin_created, "Admin instance should be created for the superuser")
        admin_instance = Admin.objects.get(username=self.superuser.username)
        self.assertTrue(admin_instance.is_superuser, "Admin should have is_superuser set to True")
        self.assertTrue(admin_instance.is_staff, "Admin should have is_staff set to True")

    # Test for customer string method
    def test_customer_str(self):
        self.assertEqual(str(self.customer), 'John Doe')

    # Test for customer creation function
    def test_customer_creation_function(self):
        create_customer(sender=self.user, instance=self.user, created=True)
        self.assertTrue(Customer.objects.filter(user=self.user).exists())

    # Test for supplier string method
    def test_supplier_str(self):
        self.assertEqual(str(self.supplier), 'ABC Supplier')

# Tests for users admin
class TestUsersAdmin(TestCase):

    # Setup before tests
    def setUp(self):
        self.site = AdminSite()
        self.supplier_admin = SupplierAdmin(Supplier, self.site)
        self.customer_admin = CustomerAdmin(Customer, self.site)
        self.customer = Customer(first_name='John', last_name='Doe', email='john.doe@example.com', phone_number='+12156783467')
        self.supplier = Supplier(name='ABC Supplier', location='Somewhere', notes='test supplier notes')

    # Test admin customer custom ID
    def test_customer_admin_custom_id(self):
        self.assertEqual(self.customer_admin.custom_id(self.customer), f'143DCUS{self.customer.pk}')

    # Test admin supplier custom ID
    def test_supplier_admin_custom_id(self):
        self.assertEqual(self.supplier_admin.custom_id(self.supplier), f'143DSUP{self.supplier.pk}')

# Tests for users forms
class TestUsersForms(TestCase):

    # Setup before tests
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', email='user@example.com', password='testpassword', first_name='user', last_name='example')
  
    # Tests for login form 
    # Test form initialization
    def test_login_form_initialization(self):
        form = LoginForm()
        self.assertIn('username', form.fields.keys())
        self.assertIn('password', form.fields.keys())
     
    # Test form validation empty fields 
    def test_login_form_validation_empty_fields(self):
        data = {
            'username': '',
            'password': ''
        }
        form = LoginForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('password', form.errors)

    # Test form validation success
    def test_login_form_validation_success(self):
        data = {
            'username': self.user.username,
            'password': self.user.password
        }
        form = LoginForm(data=data)
        self.assertTrue(form.is_valid())
        
    # Tests for register form 
    # Test form initialization
    def test_register_form_initialization(self):
        form = SignUpForm()
        self.assertIn('username', form.fields.keys())
        self.assertIn('password1', form.fields.keys())
        self.assertIn('password2', form.fields.keys())
        self.assertIn('phone_number', form.fields.keys())
        self.assertIn('email', form.fields.keys())
        self.assertIn('first_name', form.fields.keys())
        self.assertIn('last_name', form.fields.keys())
     
    # Test form validation empty fields 
    def test_register_form_validation_empty_fields(self):
        data = {
            'username': '',
            'password1': '',
            'password2': '',
            'phone_number': '',
            'email': '',
            'first_name': '',
            'last_name': ''
        }
        form = SignUpForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('password1', form.errors)
        self.assertIn('password2', form.errors)
        self.assertIn('phone_number', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)

    # Test form validation fields too long
    def test_register_form_validation_fields_too_long(self):
        data = {
            'username': 'this is just a test so it is designed to fail if it is a good test and so then it will cause the form not to be valid and the due to those failures the form will not be valid and an error message will ensue',
            'password1': self.user.password,
            'password2': self.user.password,
            'phone_number': '1-425-345-6948-19371-283',
            'email': 'testthatthisistoolongsoithastobesuperlongandthentheformwillnotbevalidandthenthetestwillpassandbesuccessfulbutinordertodosoithastobeincorrectformatsoitgetspastthefirstchecksuntilitreachesthelengthcheck@example.com',
            'first_name': 'this is just a test so it is designed to fail if it is a good test and so then it will cause the form not to be valid and the due to those failures the form will not be valid and an error message will ensue',
            'last_name': 'this is just a test so it is designed to fail if it is a good test and so then it will cause the form not to be valid and the due to those failures the form will not be valid and an error message will ensue'
        }
        form = SignUpForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('phone_number', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)

    # Test form validation email format incorrect
    def test_register_form_validation_invalid_email_format(self):
        data = {
            'username': 'testuser',
            'password1': 'mismatching',
            'password2': 'passwords',
            'phone_number': '1-425-345-6948',
            'email': 'test at example dot com',
            'first_name': 'test',
            'last_name': 'user'
        }
        form = SignUpForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    # Test form validation password invalid
    def test_register_form_validation_password_invalid(self):
        data = {
            'username': 'testuser',
            'password1': 'testuser',
            'password2': 'testuser',
            'phone_number': '1-425-345-6948',
            'email': 'test@example.com',
            'first_name': 'test',
            'last_name': 'user'
        }
        form = SignUpForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    # Test form validation mismatching passwords
    def test_register_form_validation_mismatching_passwords(self):
        data = {
            'username': 'testuser',
            'password1': 'mismatching',
            'password2': 'passwords',
            'phone_number': '1-425-345-6948',
            'email': 'test@example.com',
            'first_name': 'test',
            'last_name': 'user'
        }
        form = SignUpForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    # Test form validation success
    def test_register_form_validation_success(self):
        data = {
            'username': 'yet_another_one',
            'password1': self.user.password,
            'password2': self.user.password,
            'phone_number': '1-425-345-6948',
            'email': 'test@example.com',
            'first_name': 'test',
            'last_name': 'user'
        }
        form = SignUpForm(data=data)
        self.assertTrue(form.is_valid())
        
    # Tests for update customer form 
    # Test form initialization
    def test_update_customerr_form_initialization(self):
        form = UpdateCustomerForm()
        self.assertIn('username', form.fields.keys())
        self.assertIn('phone_number', form.fields.keys())
        self.assertIn('email', form.fields.keys())
        self.assertIn('first_name', form.fields.keys())
        self.assertIn('last_name', form.fields.keys())
     
    # Test form validation empty fields 
    def test_update_customer_form_validation_empty_fields(self):
        data = {
            'username': '',
            'phone_number': '',
            'email': '',
            'first_name': '',
            'last_name': ''
        }
        form = UpdateCustomerForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('phone_number', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)

    # Test form validation fields too long
    def test_update_customer_form_validation_fields_too_long(self):
        data = {
            'username': 'this is just a test so it is designed to fail if it is a good test and so then it will cause the form not to be valid and the due to those failures the form will not be valid and an error message will ensue',
            'phone_number': '1-425-345-6948-19371-283',
            'email': 'testthatthisistoolongsoithastobesuperlongandthentheformwillnotbevalidandthenthetestwillpassandbesuccessfulbutinordertodosoithastobeincorrectformatsoitgetspastthefirstchecksuntilitreachesthelengthcheck@example.com',
            'first_name': 'this is just a test so it is designed to fail if it is a good test and so then it will cause the form not to be valid and the due to those failures the form will not be valid and an error message will ensue',
            'last_name': 'this is just a test so it is designed to fail if it is a good test and so then it will cause the form not to be valid and the due to those failures the form will not be valid and an error message will ensue'
        }
        form = UpdateCustomerForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('phone_number', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)

    # Test form validation email format incorrect
    def test_update_customer_form_validation_invalid_email_format(self):
        data = {
            'username': 'testuser',
            'phone_number': '1-425-345-6948',
            'email': 'test at example dot com',
            'first_name': 'test',
            'last_name': 'user'
        }
        form = UpdateCustomerForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    # Test form validation success
    def test_update_customer_form_validation_success(self):
        data = {
            'username': 'yet_another_update',
            'phone_number': '98-693-694-9306',
            'email': 'updated@example.com',
            'first_name': 'updated',
            'last_name': 'updated'
        }
        form = UpdateCustomerForm(data=data)
        self.assertTrue(form.is_valid())
        
    # Tests for change password form 
    # Test form initialization
    def test_change_password_form_initialization(self):
        form = ChangePasswordForm(user=self.user)
        self.assertIn('new_password1', form.fields.keys())
        self.assertIn('new_password2', form.fields.keys())

    # Test form validation empty fields 
    def test_change_password_form_validation_empty_fields(self):
        data = {
            'new_password1': '',
            'new_password2': ''
        }
        form = ChangePasswordForm(user=self.user, data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('new_password1', form.errors)
        self.assertIn('new_password2', form.errors)

    # Test form validation password invalid
    def test_change_password_form_validation_password_invalid(self):
        data = {
            'new_password1': 'testuser',
            'new_password2': 'testuser',
        }
        form = ChangePasswordForm(user=self.user, data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('new_password2', form.errors)

    # Test form validation mismatching passwords
    def test_change_password_form_validation_mismatching_passwords(self):
        data = {
            'new_password1': 'mismatching',
            'new_password2': 'passwords',
        }
        form = ChangePasswordForm(user=self.user, data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('new_password2', form.errors)

    # Test form validation success
    def test_change_password_form_validation_success(self):
        data = {
            'new_password1': 'new_1234567890',
            'new_password2': 'new_1234567890'
        }
        form = ChangePasswordForm(user=self.user, data=data)
        self.assertTrue(form.is_valid())

class TestUsersViews(TestCase):

    # Setup before tests
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', email='user@example.com', password='testpassword', first_name='user', last_name='example')
        self.customer = Customer(first_name='John', last_name='Doe', email='john.doe@example.com', phone_number='+12156783467')

    ## Tests for login view
    # Test for login view rendering success
        
    # Test for login view empty fields
    
    # Test for login view incorrect credentials
        
    # Test for login view success
        
    ## Tests for logout view
    # Test for logout view success
    
    ## Tests for register view
    # Test for register view rendering success
        
    # Test for register view success
        
    ## Tests for update customer view
    # Test for update customer view redirect

    # Test for update customer view rendering success
        
    # Test for update customer view success
        
    ## Tests for change password view
    # Test for change password view redirect
    
    # Test for change password view rendering success
        
    # Test for change password view success
        
    ## Tests for update address view
    # Test for update address view redirect
        
    # Test for update address view rendering success
        
    # Test for update address view success
