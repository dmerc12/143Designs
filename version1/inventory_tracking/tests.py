from .models import Product, Design, Purchase, PurchaseProduct, PurchaseDesign
from .admin import ProductAdmin, DesignAdmin, PurchaseAdmin
from order_tracking.models import OrderProduct, Order
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from users.models import Supplier, Customer
from django.test import RequestFactory
from django.test import TestCase

class TestInventoryTrackingModels(TestCase):
    pass

class TestInventoryTrackingAdmin(TestCase):
    pass
