from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='users-register'),
    path('update/', views.update_user, name='users-update'),
    path('change-password/', views.change_password, name='users-change-password'),
]
