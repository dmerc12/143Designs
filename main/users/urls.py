from .views import login_user, logout_user, register, register_admin, admin_home, update_user, delete_user, delete_admin, change_password
from django.urls import path

# URL's for Users app
urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('admin/register/', register_admin, name='register-admin'),
    path('admin/', admin_home, name='admin-home'),
    path('update/', update_user, name='update-user'),
    path('delete/', delete_user, name='delete-user'),
    path('admin/delete/<int:admin_id>', delete_admin, name='delete-admin'),
    path('change/password/', change_password, name='change-password')
]
