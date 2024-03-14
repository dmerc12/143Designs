from django.conf.urls.static import static
from site_management.views import home
from django.urls import path, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('site/', include('site_management.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
