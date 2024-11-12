from django.shortcuts import render, redirect, get_object_or_404
from core.decorators import admin_only, check_group
from django.contrib import messages
from django.core.paginator import Paginator

from shop.models import Product
from admin_panel.forms import ProductCreationForm, EditProductForm
from admin_panel.filters import  ProductFilter


@admin_only
def products(request):
    products = Product.objects.all()
    
    product_filter = ProductFilter(request.GET, queryset=products)
    filtered_products  = product_filter.qs

    paginator = Paginator(filtered_products, 4) 
    page_number = request.GET.get('page')
    pages = paginator.get_page(page_number)

    query_params = request.GET.copy()
    if 'page' in query_params:
        query_params.pop('page') 
    filters = query_params.urlencode() 


    return render(request, 'admin_panel/shop/products.html', {
        'products': pages,
        'ProductFilter': product_filter,
        'pages': pages,
        'filters': filters,

    })


@admin_only
def add_product(request):

    form = ProductCreationForm()
    if request.method == 'POST':
        form = ProductCreationForm(request.POST, request.FILES)
       
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            messages.success(request, 'The product was added successfully')
            return redirect('admin_panel:products')

        

    return render(request, 'admin_panel/shop/add_product.html', {
        'ProductCreationForm': form
    })



@admin_only
def edit_product(request, pk):

    product = Product.objects.get(id=pk)  
    
    form = EditProductForm(instance=product)

    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES, instance=product)
        
        if form.is_valid():
            form.save()
   
            messages.success(request, 'The product was edited!')
            return redirect('admin_panel:products')
        
    return render(request, 'admin_panel/shop/edit_product.html', {
        'EditProductForm': form,
        'product': product,
    })