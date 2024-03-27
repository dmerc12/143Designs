from .views import admin_home, register_admin, activate_admin, deactivate_admin, admin_reset_password
from .views import login_user, logout_user, register, update_user, delete_user, change_password
from .views import customer_home, create_customer, edit_customer
from django.urls import path

# URL's for Users app
urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('change/password/', change_password, name='change-password'),
    path('update/', update_user, name='update-user'),
    path('delete/', delete_user, name='delete-user'),
    path('admin/', admin_home, name='admin-home'),
    path('admin/register/', register_admin, name='register-admin'),
    path('admin/activate/<int:admin_id>/', activate_admin, name='activate-admin'),
    path('admin/deactivate/<int:admin_id>/', deactivate_admin, name='deactivate-admin'),
    path('admin/reset/password/<int:user_id>/', admin_reset_password, name='admin-reset-password'),
    path('customer/', customer_home, name='customer-home'),
    path('customer/create/', create_customer, name='create-customer'),
    path('customer/edit/<int:customer_id>/', edit_customer, name='edit-customer'),
]
