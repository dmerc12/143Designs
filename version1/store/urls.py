from django.urls import path
from .views import *

urlpatterns = [
    path('', store_home, name='store-home'),
    path('item/<int:item_id>/', item_detail, name='item-detail')
]
