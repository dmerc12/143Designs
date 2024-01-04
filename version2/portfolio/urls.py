from django.urls import path
from .review.views import review_list, review_detail, review_create, review_update, review_delete
from . import views

urlpatterns = [
    path('', views.home, name='portfolio-home'),
    path('reviews/', review_list, name='review-list'),
    path('reviews/<int:review_id>/', review_detail, name='review-detail'),
    path('reviews/create/', review_create, name='review-create'),
    path('reviews/<int:review_id>/update/', review_update, name='review-update'),
    path('reviews/<int:review_id>/delete/', review_delete, name='review-delete'),
]
