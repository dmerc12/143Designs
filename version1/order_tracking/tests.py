from inventory_tracking.models import Product, Design
from .models import Order, OrderProduct, OrderDesign
from django.contrib.admin.sites import AdminSite
from users.models import Customer
from django.test import TestCase
from .admin import OrderAdmin

class TestOrderTrackingModels(TestCase):
    pass

class TestOrderTrackingAdmin(TestCase):
    pass
