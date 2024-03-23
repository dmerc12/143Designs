from .views import admin_home, contact, messages_home
from django.urls import path

urlpatterns = [
    path('', admin_home, name='admin-home'),
    path('contact/', contact, name='contact'),
    path('messages/', messages_home, name='messages-home'),
]
