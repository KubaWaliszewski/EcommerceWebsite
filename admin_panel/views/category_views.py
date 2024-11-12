from django.shortcuts import render, redirect, get_object_or_404
from core.decorators import admin_only, check_group
from django.contrib import messages
from django.core.paginator import Paginator

from shop.models import Category
from admin_panel.forms import AddCategoryForm
from admin_panel.filters import CategoryFilter


@admin_only
@check_group(allowed_groups=['Agent'])
def category(request):
    #Add Category
    form = AddCategoryForm()
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if 'delete_category' in request.POST:
            category_id = request.POST.get('delete_category')
            category = get_object_or_404(Category, id=category_id)
            category.delete()
            messages.success(request, 'The category was deleted successfully!')
            return redirect('admin_panel:category')
        
        
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The category was added successfully')
            return redirect('admin_panel:category')
        
    # Category list
    category = Category.objects.all()

    len_category = len(category)

    category_filter = CategoryFilter(request.GET, queryset=category)
    filtered_users  = category_filter.qs

    paginator = Paginator(filtered_users, 5) 
    page_number = request.GET.get('page')
    pages = paginator.get_page(page_number)

    query_params = request.GET.copy()
    if 'page' in query_params:
        query_params.pop('page') 
    filters = query_params.urlencode() 

    return render(request, 'admin_panel/shop/category.html', {
        'AddCategoryForm': form,
        'category': pages,
        'CategoryFilter': category_filter,
        'pages': pages,
        'filters': filters,
        'len_category': len_category,
    })