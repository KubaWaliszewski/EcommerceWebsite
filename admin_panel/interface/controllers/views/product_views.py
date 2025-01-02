from django.shortcuts import render, redirect

from core.interface.decorators import admin_only
from admin_panel.application.use_cases.utils import extract_filters_from_query_params, get_filtered_and_paginated_queryset
from admin_panel.application.use_cases.product_usecases import AddProductUseCase, EditProductUseCase
from admin_panel.infrastructure.repositories.product_repository import ProductRepository


@admin_only
def products(request):
    page_number = request.GET.get('page', 1)

    paginated_products, _, product_filter, products = get_filtered_and_paginated_queryset(
        query_params=request.GET,
        repository_method=ProductRepository.get_filtered,
        page_number=page_number,
        per_page=5,
    )

    filters = extract_filters_from_query_params(request.GET) 


    return render(request, 'admin_panel/shop/products.html', {
        'products': paginated_products,
        'ProductFilter': product_filter,
        'pages': paginated_products,
        'filters': filters,
        'len_products': len(products),
    })


@admin_only
def add_product(request):
    success, result = AddProductUseCase.execute(request)

    if success:
        return redirect('admin_panel:products')

    return render(request, 'admin_panel/shop/add_product.html', {
        'ProductCreationForm': result
    })


@admin_only
def edit_product(request, pk):
    success, result = EditProductUseCase.execute(request, pk)
    if success:
        return redirect('admin_panel:products')
    form, product = result

    return render(request, 'admin_panel/shop/edit_product.html', {
        'EditProductForm': form,
        'product': product,
    })



