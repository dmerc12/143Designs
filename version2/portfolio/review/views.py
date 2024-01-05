from django.shortcuts import render, get_object_or_404, redirect
from ..models import Review
from .forms import CreateReviewForm, UpdateReviewForm
from .middleware import ReviewMiddleware

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'portfolio/review/list.html', {'reviews': reviews})

def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'portfolio/review/detail.html', {'review': review})

def create_review(request):
    if request.method == 'POST':
        form = CreateReviewForm(request.POST)
        if form.is_valid():
            ReviewMiddleware.create_review(request, form)
            return redirect('home')
    else:
        form = CreateReviewForm()

    return render(request, 'main/home.html', {'form': form, 'action': 'create'})

def update_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if request.method == 'POST':
        form = UpdateReviewForm(request.POST, instance=review)
        if form.is_valid():
            ReviewMiddleware.update_review(request, form, review_id)
            return redirect('review-list')
    else:
        form = UpdateReviewForm(instance=review)

    return render(request, 'portfolio/review/update.html', {'form': form, 'action': 'Update'})

def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if request.method == 'POST':
        ReviewMiddleware.delete_review(request, review)
        return redirect('review-list')

    return render(request, 'portfolio/review/delete.html', {'review': review})
