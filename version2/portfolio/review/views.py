from django.shortcuts import render, get_object_or_404, redirect
from ..models import Review
from .forms import ReviewForm 
from .middleware import ReviewMiddleware

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'portfolio/review/list.html', {'reviews': reviews})

def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'portfolio/review/detail.html', {'review': review})

def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            ReviewMiddleware.create_review(request, form)
            return redirect('review-list')
    else:
        form = ReviewForm()

    return render(request, 'portfolio/review/form.html', {'form': form, 'action': 'Create'})

def review_update(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            ReviewMiddleware.update_review(request, form)
            return redirect('review-list')
    else:
        form = ReviewForm(instance=review)

    return render(request, 'portfolio/review/form.html', {'form': form, 'action': 'Update'})

def review_delete(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if request.method == 'POST':
        ReviewMiddleware.delete_review(request, review)
        return redirect('review-list')

    return render(request, 'portfolio/review/delete.html', {'review': review})
