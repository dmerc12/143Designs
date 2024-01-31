from django.contrib.admin.sites import AdminSite
from .admin import CustomerAdmin, SupplierAdmin
from .models import Admin, Customer, Supplier
from django.test import TestCase

class TestUsersModels(TestCase):
    def test_admin_save(self):
        admin = Admin(username='testadmin', email='testadmin@example.com')
        admin.save()
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

    def test_admin_str(self):
        admin = Admin(username='testadmin', email='testadmin@example.com')
        self.assertEqual(str(admin), 'testadmin')

    def test_customer_str(self):
        customer = Customer(first_name='John', last_name='Doe', email='john.doe@example.com', phone_number='+12156783467')
        self.assertEqual(str(customer), 'John Doe')

    def test_supplier_str(self):
        supplier = Supplier(name='ABC Supplier', location='Somewhere', notes='test supplier notes')
        self.assertEqual(str(supplier), 'ABC Supplier')

class TestUsersAdmin(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_customer_admin_custom_id(self):
        customer_admin = CustomerAdmin(Customer, self.site)
        customer = Customer(first_name='John', last_name='Doe', email='john.doe@example.com', phone_number='+12156783467')
        self.assertEqual(customer_admin.custom_id(customer), f'143DCUS{customer.pk}')

    def test_supplier_admin_custom_id(self):
        supplier_admin = SupplierAdmin(Supplier, self.site)
        supplier = Supplier(name='ABC Supplier', location='Somewhere', notes='test supplier notes')
        self.assertEqual(supplier_admin.custom_id(supplier), f'143DSUP{supplier.pk}')
