from django.shortcuts import render

from shop.application.use_cases.search_products_usecase import SearchProductsUseCase
from shop.infrastructure.repositories.product_repository import ProductRepository


def search_view(request):
    query = request.GET.get('query', '').strip()
    repository = ProductRepository()  
    use_case = SearchProductsUseCase(repository)
    products = use_case.execute(query)

    return render(request, 'shop/search.html', {
        'query': query,
        'products': products,
    })