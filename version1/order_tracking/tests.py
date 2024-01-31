from inventory_tracking.models import Size, Product, Design
from .models import Order, OrderProduct, OrderDesign
from django.contrib.admin.sites import AdminSite
from users.models import Customer
from django.test import TestCase
from .admin import OrderAdmin

class TestOrderTrackingModels(TestCase):
    def test_order_str(self):
        customer = Customer.objects.create(first_name='test', last_name='test', email='test@email.com', phone_number='+14053086584')
        order = Order.objects.create(customer=customer, short_description='test')
        self.assertEqual(str(order), f"143D{order.pk} - {order.short_description} - ${order.total}")

    def test_order_product_delete(self):
        pass

    def test_order_product_str(self):
        customer = Customer.objects.create(first_name='test', last_name='test', email='test@email.com', phone_number='+14053086584')
        order = Order.objects.create(customer=customer, short_description='test')
        size = Size.objects.create(name='test')
        product = Product.objects.create(name='test', material='test', color='test', size=size, price=2.25)
        order_product = OrderProduct.objects.create(order=order, item=product, quantity=5)
        self.assertEqual(str(order_product), f"{order_product.order} - {order_product.quantity} of {order_product.item}")

    def test_order_design_save(self):
        pass

    def test_order_design_delete(self):
        pass

    def test_order_design_str(self):
        customer = Customer.objects.create(first_name='test', last_name='test', email='test@email.com', phone_number='+14053086584')
        order = Order.objects.create(customer=customer, short_description='test')
        design = Design.objects.create(name='test', image='/Users/dylanmercer12/Desktop/Projects/143Designs/download.webp', price=1.25, cost=0.75)
        order_design = OrderDesign.objects.create(order=order, design=design, quantity=5)
        self.assertEqual(str(order_design), f"{order_design.order} - {order_design.quantity} of {order_design.design}")

class MockRequest(object):
    pass

request = MockRequest()

class TestOrderTrackingAdmin(TestCase):
    def setUp(self):
        self.site = OrderAdmin(Order, AdminSite())

    def test_mark_complete(self):
        customer = Customer.objects.create(first_name='test', last_name='test', email='test@email.com', phone_number='+14053086584')
        order = Order.objects.create(customer=customer, short_description='test')
        self.site.mark_complete(self.site, request, queryset=Order.objects.filter(pk=order.pk))
        self.assertTrue(order.complete)

    def test_mark_incomplete(self):
        customer = Customer.objects.create(first_name='test', last_name='test', email='test@email.com', phone_number='+14053086584')
        order = Order.objects.create(customer=customer, short_description='test')
        self.site.mark_complete(self.site, request, queryset=Order.objects.filter(pk=order.pk))
        self.site.mark_incomplete(self.site, request, queryset=Order.objects.filter(pk=order.pk))
        self.assertFalse(order.complete)

    def test_mark_paid(self):
        customer = Customer.objects.create(first_name='test', last_name='test', email='test@email.com', phone_number='+14053086584')
        order = Order.objects.create(customer=customer, short_description='test')
        self.site.mark_paid(self.site, request, queryset=Order.objects.filter(pk=order.pk))
        self.assertTrue(order.paid)

    def test_mark_unpaid(self):
        customer = Customer.objects.create(first_name='test', last_name='test', email='test@email.com', phone_number='+14053086584')
        order = Order.objects.create(customer=customer, short_description='test')
        self.site.mark_paid(self.site, request, queryset=Order.objects.filter(pk=order.pk))
        self.site.mark_unpaid(self.site, request, queryset=Order.objects.filter(pk=order.pk))
        self.assertFalse(order.paid)

    def test_order_admin_custom_id(self):
        customer = Customer.objects.create(first_name='test', last_name='test', email='test@email.com', phone_number='+14053086584')
        order = Order.objects.create(customer=customer, short_description='test')
        self.assertEqual(str(self.site.custom_id_display(order)), f'143DORD{order.pk}')
