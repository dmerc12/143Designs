from .admin import SizeAdmin, ProductAdmin, DesignAdmin, PurchaseAdmin, SizeNameFilter
from .models import Size, Product, Design, Purchase, PurchaseProduct, PurchaseDesign
from order_tracking.models import OrderProduct, Order
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from users.models import Supplier, Customer
from django.test import RequestFactory
from django.test import TestCase

class TestInventoryTrackingModels(TestCase):
    def test_size_str(self):
        size = Size.objects.create(name='test')
        self.assertEqual(str(size), 'test')
    
    def test_product_str(self):
        size = Size.objects.create(name='test')
        product = Product.objects.create(name='test', material='test', color='test', size=size, price=2.25)
        self.assertEqual(str(product), 'test test test - $2.25')

    def test_design_str(self):
        design = Design.objects.create(name='test', image='/Users/dylanmercer12/Desktop/Projects/143Designs/download.webp', price=1.25, cost=0.75)
        self.assertEqual(str(design), 'test - $1.25')

    def test_purchase_calculate_subtotal(self):
        size = Size.objects.create(name='test')
        product = Product.objects.create(name='test', material='test', color='test', size=size, price=2.25)
        design = Design.objects.create(name='test', image='/Users/dylanmercer12/Desktop/Projects/143Designs/download.webp', price=1.25, cost=0.75)
        supplier = Supplier.objects.create(name='test', location='test')
        purchase = Purchase.objects.create(supplier=supplier)
        PurchaseProduct.objects.create(purchase=purchase, product=product)
        PurchaseDesign.objects.create(purchase=purchase, design=design)
        purchase.calculate_subtotal()
        self.assertEqual(purchase.subtotal, (product.price + design.price))

    def test_purchase_str(self):
        supplier = Supplier.objects.create(name='test', location='test')
        purchase = Purchase.objects.create(supplier=supplier)
        self.assertEqual(str(purchase), f'143DPUR{purchase.pk}')

    def test_purchase_product_save(self):
        size = Size.objects.create(name='test')
        product = Product.objects.create(name='test', material='test', color='test', size=size, price=2.25)
        supplier = Supplier.objects.create(name='test', location='test')
        purchase = Purchase.objects.create(supplier=supplier)
        PurchaseProduct.objects.create(purchase=purchase, product=product)
        self.assertEqual(purchase.subtotal, product.price)

    def test_purchase_product_delete(self):
        size = Size.objects.create(name='test')
        product = Product.objects.create(name='test', material='test', color='test', size=size, price=2.25)
        supplier = Supplier.objects.create(name='test', location='test')
        purchase = Purchase.objects.create(supplier=supplier)
        purchase_product = PurchaseProduct.objects.create(purchase=purchase, product=product)
        purchase_product.delete()
        self.assertEqual(purchase.subtotal, 0)

    def test_purchase_design_save(self):
        design = Design.objects.create(name='test', image='/Users/dylanmercer12/Desktop/Projects/143Designs/download.webp', price=1.25, cost=0.75)
        supplier = Supplier.objects.create(name='test', location='test')
        purchase = Purchase.objects.create(supplier=supplier)
        PurchaseDesign.objects.create(purchase=purchase, design=design)
        self.assertEqual(purchase.subtotal, design.price)

    def test_purchase_design_delete(self):
        design = Design.objects.create(name='test', image='/Users/dylanmercer12/Desktop/Projects/143Designs/download.webp', price=1.25, cost=0.75)
        supplier = Supplier.objects.create(name='test', location='test')
        purchase = Purchase.objects.create(supplier=supplier)
        purchase_design = PurchaseDesign.objects.create(purchase=purchase, design=design)
        purchase_design.delete()
        self.assertEqual(purchase.subtotal, 0)
    
class TestInventoryTrackingAdmin(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.user = User.objects.create_user(username='admin', password='admin')
        self.client.login(username='admin', password='admin')
        self.factory = RequestFactory()

    def test_size_admin_custom_id(self):
        size_admin = SizeAdmin(Size, self.site)
        size = Size.objects.create(name='test')
        self.assertEqual(size_admin.custom_id(size), f'143DS{size.pk}')

    def test_size_admin_filter_lookup(self):
        size_admin = SizeAdmin(Size, self.site)
        size_name_filter = SizeNameFilter(request=None, params={}, model=Size, model_admin=size_admin)
        lookups = size_name_filter.lookups(request=self.factory.get('/admin/'), model_admin=size_admin)
        expected_lookups = [(size.name, size.name) for size in Size.objects.all()]
        self.assertEqual(list(lookups), expected_lookups)

    def test_size_admin_filter_queryset(self):
        size_admin = SizeAdmin(Size, self.site)
        size_name_filter = SizeNameFilter(request=self.factory.get('/admin/'), params={}, model=Size, model_admin=size_admin)
        size = Size.objects.create(name='test')
        queryset = size_name_filter.queryset(None, Size.objects.all())
        self.assertEqual(list(queryset), [size])

    def test_product_admin_custom_id(self):
        product_admin = ProductAdmin(Product, self.site)
        size = Size.objects.create(name='test')
        product = Product.objects.create(name='test', material='test', color='test', size=size, price=2.25)
        self.assertEqual(product_admin.custom_id(product), f'143DPROD{product.pk}')

    def test_product_admin_total_quantity_in_stock(self):
        product_admin = ProductAdmin(Product, self.site)
        size = Size.objects.create(name='test')
        product = Product.objects.create(name='test', material='test', color='test', size=size, price=2.25)
        supplier = Supplier.objects.create(name='test', location='test')
        purchase = Purchase.objects.create(supplier=supplier)
        purchase_product = PurchaseProduct.objects.create(purchase=purchase, product=product, quantity=10)
        customer = Customer.objects.create(first_name='test', last_name='test', email='test@email.com', phone_number='+14053086584')
        order = Order.objects.create(customer=customer, short_description='test')
        OrderProduct.objects.create(order=order, item=product, quantity=5)
        total_quantity = product_admin.total_quantity_in_stock(obj=product)
        self.assertEqual(total_quantity, purchase_product.quantity)

    def test_design_admin_custom_id(self):
        design_admin = DesignAdmin(Design, self.site)
        design = Design.objects.create(name='test', image='/Users/dylanmercer12/Desktop/Projects/143Designs/download.webp', price=1.25, cost=0.75)
        self.assertEqual(design_admin.custom_id(design), f'143DDES{design.pk}')

    def test_design_admin_image_preview(self):
        design_admin = DesignAdmin(Design, self.site)
        design = Design.objects.create(name='test', image='/Users/dylanmercer12/Desktop/Projects/143Designs/download.webp', price=1.25, cost=0.75)
        preview = design_admin.image_preview(design)
        self.assertIn('img', preview)
        self.assertIn(design.image.url, preview)

    def test_purchase_admin_custom_id(self):
        purchase_admin = PurchaseAdmin(Purchase, self.site)
        supplier = Supplier.objects.create(name='test', location='test')
        purchase = Purchase.objects.create(supplier=supplier)
        self.assertEqual(purchase_admin.custom_id(purchase), f'143DPUR{purchase.pk}')
