from .models import Product, ProductSize, Design, Purchase, PurchaseProduct, PurchaseDesign
from users.models import Supplier
from django.test import TestCase

# Tests for inventory models
class TestInventoryModels(TestCase):

    def setUp(self):
        self.product = Product.objects.create(name='name', material='material', color='color')
        self.size = ProductSize.objects.create(size='size', cost=5.75, price=6.25, product=self.product)
        self.design = Design.objects.create(name='name', cost=4.25, price=4.75, image='path/test.png')
        self.supplier = Supplier.objects.create(name='name', location='location')
        self.purchase = Purchase.objects.create(supplier=self.supplier)
        self.purchase_product = PurchaseProduct.objects.create(purchase=self.purchase, product=self.product, size=self.size, quantity=1)
        self.purchase_design = PurchaseDesign.objects.create(purchase=self.purchase, design=self.design, quantity=1)

    ## Tests for product model
    ### Test for model string method
    def test_product_str(self):
        self.assertEqual(str(self.product), f'{self.product.color} {self.product.material} {self.product.name}')

    ### Test for get product sizes method
    def test_product_sizes(self):
        sizes = self.product.get_product_sizes()
        self.assertIn(sizes, self.size)

    ## Tests for product size model
    ### Test for model string method
    def test_product_size_str(self):
        self.assertEqual(str(self.size), f'{self.size.size} ${self.size.price} - {self.size.product.__str__()}')

    ## Tests from design model
    ### Test for model string method
    def test_design_str(self):
        self.assertEqual(str(self.design), f'{self.design.name} - ${self.design.price}')

    ### Test for image preview method
    def test_image_preview(self):
        preview = self.design.image_preview()
        self.assertEqual(preview, f'<img src="{self.design.image.url}" style="max-width:200px; max-height: 200px"/>')

    ## Tests for purchase model
    ### Test for model string method
    def test_purchase_str(self):
        self.assertEqual(str(self.purchase), f'143DPUR{self.purchase.pk}')

    ### Test for calculate subtotal method
    def test_calculate_subtotal(self):
        subtotal = self.purchase.calculate_subtotal()
        self.assertEqual(subtotal, self.size.cost + self.design.cost)

    ## Tests for purchase product model
    ### Test for save method
    def test_purchase_product_save(self):
        PurchaseProduct.objects.create(purchase=self.purchase, product=self.product, size=self.size, quantity=2)
        self.assertEqual(self.purchase.subtotal, (3 * self.size.cost) + self.design.cost)

    ### Test for delete method
    def test_purchase_product_delete(self):
        purchase_product = PurchaseProduct.objects.create(purchase=self.purchase, product=self.product, size=self.size, quantity=2)
        purchase_product.delete()
        self.assertEqual(self.purchase.subtotal, self.size.cost + self.design.cost)

    ## Tests for purchase design
    ### Test for save method
    def test_purchase_design_save(self):
        PurchaseDesign.objects.create(purchase=self.purchase, design=self.design, quantity=3)
        self.assertEqual(self.purchase.subtotal, (4 * self.design.cost) + self.size.cost)

    ### Test for delete method
    def test_purchase_design_delete(self):
        purchase_design = PurchaseDesign.objects.create(purchase=self.purchase, design=self.design, quantity=3)
        purchase_design.delete()
        self.assertEqual(self.purchase.subtotal, self.size.cost + self.design.cost)
