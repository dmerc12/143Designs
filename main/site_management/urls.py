from .views import admin_home, contact, messages_home, delete_message
from django.urls import path

urlpatterns = [
    path('', admin_home, name='admin'),
    path('contact/', contact, name='contact'),
    path('messages/', messages_home, name='messages-home'),
    path('messages/delete/<int:message_id>', delete_message, name='delete-message'),
]
