from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from orders.models import OrderItem
from django.contrib import messages

from .forms import ReviewForm
from .models import Category, Product



def product_list(request, category_slug=None):
    category = None
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    paginator = Paginator(products, 8)
    page = request.GET.get('page')
    pages = paginator.get_page(page)

    return render(request,'shop/product_list.html', {
        'products': pages,
        'category': category,
        'categories': categories,
        'pages': pages,
    })


def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)

    category = get_object_or_404(Category, slug=category_slug)
    category_products = Product.objects.filter(category=category, is_available=True)[:8] if category else []

    return render(request, 'shop/product_detail.html', {
        'product': product,
        'category_products': category_products,
    })


def search(request):
    query = request.GET.get('query', '')

    if not query:
        products = []
    else:
        products = Product.objects.filter(is_available=True).filter(
            Q(name__icontains=query) | Q(description__icontains=query)
            )

    return render(request , 'shop/search.html', {
        'query': query,
        'products': products,
    })


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    has_purchased = OrderItem.objects.filter(order__user=request.user, product=product).exists()
    
    if not has_purchased:
        messages.error(request, "You can't review this product because you haven't purchased it.")
        return redirect('shop:product_detail', category_slug=product.category.slug, slug=product.slug)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been added!')
            return redirect('shop:product_detail', category_slug=product.category.slug, slug=product.slug)
    else:
        form = ReviewForm()

    return render(request, 'shop/add_review.html', {
        'product': product,
        'form': form
    })