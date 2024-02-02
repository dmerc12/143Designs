from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='store-home'),
    path('contact/', contact, name='contact')
]