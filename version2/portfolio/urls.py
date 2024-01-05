from django.urls import path
from .review.views import review_list, review_detail, create_review, update_review, delete_review
from . import views

urlpatterns = [
    path('', views.home, name='portfolio-home'),
    path('reviews/', review_list, name='review-list'),
    path('reviews/<int:review_id>/', review_detail, name='review-detail'),
    path('reviews/create/', create_review, name='review-create'),
    path('reviews/<int:review_id>/update/', update_review, name='review-update'),
    path('reviews/<int:review_id>/delete/', delete_review, name='review-delete'),
]
