from django.shortcuts import render, redirect
from core.interface.decorators import admin_only, check_group
from django.contrib import messages

from admin_panel.interface.controllers.forms import AddCategoryForm
from admin_panel.infrastructure.repositories.category_repository import CategoryRepository
from admin_panel.application.use_cases.category_usecases import add_category, delete_category
from admin_panel.application.use_cases.utils import extract_filters_from_query_params, get_filtered_and_paginated_queryset


@admin_only
@check_group(allowed_groups=['Agent'])
def category(request):
    form = AddCategoryForm()
    if request.method == 'POST':
        if 'delete_category' in request.POST:
            category_id = request.POST.get('delete_category')
            delete_category(category_id)
            messages.success(request, 'The category was deleted successfully!')
            return redirect('admin_panel:category')
        
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            add_category(form.cleaned_data)
            messages.success(request, 'The category was added successfully')
            return redirect('admin_panel:category')

    page_number = request.GET.get('page', 1)

    paginated_category, _, category_filter, categories = get_filtered_and_paginated_queryset(
        query_params=request.GET,
        repository_method=CategoryRepository.get_filtered,
        page_number=page_number,
        per_page=4
    )

    filters = extract_filters_from_query_params(request.GET)

    return render(request, 'admin_panel/shop/category.html', {
        'AddCategoryForm': form,
        'category': paginated_category,
        'CategoryFilter': category_filter,
        'pages': paginated_category,
        'filters': filters,
        'len_category': len(categories),
    })


