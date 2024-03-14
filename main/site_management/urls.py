from .views import admin_home
from django.urls import path

urlpatterns = [
    path('admin/', admin_home, name='admin-home'),
]
