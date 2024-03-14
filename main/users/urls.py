from .views import home, admin_home, login_user, logout_user, register, update_user, delete_user, change_password
from django.urls import path

# URL's for Users app
urlpatterns = [
    path('admin/', admin_home, name='admin-home'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('update/', update_user, name='update-user'),
    path('delete/', delete_user, name='delete-user'),
    path('change/password/', change_password, name='change-password')
]
