from ..models import Review

class ReviewMiddleware:

    @staticmethod
    def create_review(request, form):
        form.save()

    @staticmethod
    def update_review(request, form):
        form.save()

    @staticmethod
    def delete_review(request, review):
        review.delete()
