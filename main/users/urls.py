from .views import login_user, logout_user, register, register_admin, update_user, delete_user, change_password
from django.urls import path

# URL's for Users app
urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('register/admin/', register_admin, name='register-admin'),
    path('update/', update_user, name='update-user'),
    path('delete/', delete_user, name='delete-user'),
    path('change/password/', change_password, name='change-password')
]
