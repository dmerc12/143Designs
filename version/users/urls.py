from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='manage-users'),
    path('add/', views.add_user, name='add-user'),
    path('update/', views.update_user, name='update-user'),
    path('change-password/', views.change_password, name='change-password'),
    path('delete/', views.delete_user, name='delete-user'),
]
