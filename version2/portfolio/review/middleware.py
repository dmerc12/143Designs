from ..models import Review
from django.contrib import messages
from django.shortcuts import redirect

class ReviewMiddleware:

    @staticmethod
    def create_review(request, form):
        review = Review()
        review.first_name = form.cleaned_data['first_name']
        review.last_name = form.cleaned_data['last_name']
        review.subject = form.cleaned_data['subject']
        review.text = form.cleaned_data['text']
        review.rating = form.cleaned_data['rating']
        review.save()
        messages.success(request, 'Thank you, your review has been created!')

    @staticmethod
    def update_review(request, form, review_id):
        try:
            review = Review.objects.get(pk=review_id)
            print(f"Current status: {review.status}")
            review.status = form.cleaned_data['status']
            review.save(update_fields=['status'])
            print(f"Updated status: {review.status}")
            messages.success(request, 'The status of this review has been updated!')
        except Exception as error:
            messages.error(request, str(error))

    @staticmethod
    def delete_review(request, review):
        review.delete()
        messages.success(request, 'This review has been deleted!')
