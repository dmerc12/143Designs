from .models import Size, Product, Design, Purchase, PurchaseProduct, PurchaseDesign
from users.models import Supplier
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
    