from django.contrib.admin.sites import AdminSite
from .admin import CustomerAdmin, SupplierAdmin
from django.contrib.auth.models import User
from django.test import TestCase
from .models import *

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
        pass
