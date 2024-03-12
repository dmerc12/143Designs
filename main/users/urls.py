from .views import home, admin_home, login_user, logout_user
from django.urls import path

# URL's for Users app
urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin_home, name='admin-home'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout')
]
