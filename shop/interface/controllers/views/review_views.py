from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ..form.review_form import ReviewForm
from shop.application.use_cases.add_review_usecase import AddReviewUseCase
from shop.infrastructure.repositories.review_repository import ReviewRepository


@login_required
def add_review(request, product_id):
    repository = ReviewRepository()
    use_case = AddReviewUseCase(repository)

    form = ReviewForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        try:
            product = repository.get_product_by_id(product_id)
            use_case.execute(request.user, product_id, form.cleaned_data)
            messages.success(request, "Review added!")
            return redirect('shop:product_detail', category_slug=product.category.slug, slug=product.slug)  
        except PermissionError as e:
            messages.error(request, str(e))
        return redirect('shop:product_detail', category_slug=product.category.slug, slug=product.slug)

    return render(request, 'shop/add_review.html', {'form': form})