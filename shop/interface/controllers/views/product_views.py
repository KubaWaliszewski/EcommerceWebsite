from django.shortcuts import render
from django.core.paginator import Paginator

from shop.application.use_cases.products_usecase import ListProductsUseCase, GetProductDetailUseCase
from shop.infrastructure.repositories.product_repository import ProductRepository


def product_list(request, category_slug=None):
    repository = ProductRepository()
    use_case = ListProductsUseCase(repository)
    products, category, categories = use_case.execute(category_slug)

    paginator = Paginator(products, 8)
    page = request.GET.get('page')
    pages = paginator.get_page(page)

    return render(request, 'shop/product_list.html', {
        'products': pages,
        'category': category,
        'categories': categories,
        'pages': pages,
    })


def product_detail(request, category_slug, slug):
    repository = ProductRepository()
    use_case = GetProductDetailUseCase(repository)
    product, category_products = use_case.execute(category_slug, slug)

    return render(request, 'shop/product_detail.html', {
        'product': product,
        'category_products': category_products,
    })
