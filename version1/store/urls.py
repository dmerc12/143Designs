from django.urls import path
from .views import *

urlpatterns = [
    path('', store_home, name='store-home'),
]
