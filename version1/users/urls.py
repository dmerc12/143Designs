from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_customer, name='login'),
    path('logout/', logout_customer, name='logout'),
]
