from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_customer, name='login'),
    path('logout/', logout_customer, name='logout'),
    path('register/', register_customer, name='register'),
    path('update/', update_customer, name='update-customer'),
    path('change-password/', change_password, name='change-password'),
]
