from site_management import views as site_views
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', site_views.home, name='home'),
    path('contact/', site_views.contact, name='contact'),
    path('store/', include('store.urls')),
    path('users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
