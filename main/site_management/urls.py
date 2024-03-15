from .views import admin_home, contact
from django.urls import path

urlpatterns = [
    path('admin/', admin_home, name='admin-home'),
    path('contact/', contact, name='contact'),
]
