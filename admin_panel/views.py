from django.shortcuts import render, redirect, get_object_or_404
from core.decorators import admin_only, check_group
from django.contrib import messages
from django.core.paginator import Paginator

from account.models import CustomUser
from shop.models import Product, Category
from .forms import UserCreationForm, EditUserForm, ProductCreationForm, EditProductForm, AddCategoryForm
from .filters import UserFilter, ProductFilter, CategoryFilter
from orders.models import Order


@admin_only
def admin_dashboard(request):
    
    #Customers panel
    users = CustomUser.objects.filter(role='client')
    len_users = len(users)
    user_filter = UserFilter(request.GET, queryset=users)
    filtered_users  = user_filter.qs

    # Paginate users (customers)
    paginator = Paginator(filtered_users, 5) 
    page_number = request.GET.get('page')
    pages = paginator.get_page(page_number)

    query_params = request.GET.copy()
    if 'page' in query_params:
        query_params.pop('page') 
    filters = query_params.urlencode() 

    #Orders panel
    orders = Order.objects.all()
    order_delivered = len(Order.objects.filter(status='Delivered'))
    order_pending = len(Order.objects.filter(status='Pending'))


    return render(request, 'admin_panel/dashboard.html', {
        'users': pages,
        'len_users': len_users,
        'UserFilter': user_filter,
        'pages': pages,
        'filters': filters,
        'orders': orders,
        'order_delivered': order_delivered,
        'order_pending': order_pending,
    })


@admin_only
def user_view(request, uuid):
    user = get_object_or_404(CustomUser, id=uuid)

    orders = Order.objects.filter(user=user)

    return render(request, 'admin_panel/users/user-view.html',{
        'user': user,
        'orders': orders,
    })


@admin_only
def order_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')

        if new_status in dict(Order.STATUS):
            order.status = new_status
            order.save()  
            messages.success(request, 'The order status was updated successfully!')
            return redirect('admin_panel:order_view', order_id=order.id)

        

    return render(request, 'admin_panel/orders/order-view.html', {
        'order': order,
    })


# ===============================
# Users Management Views
# ===============================


@admin_only
@check_group(allowed_groups=['Agent'])
def users(request):
    users = CustomUser.objects.all()

    user_filter = UserFilter(request.GET, queryset=users)
    filtered_users  = user_filter.qs

    paginator = Paginator(filtered_users, 10) 
    page_number = request.GET.get('page')
    pages = paginator.get_page(page_number)

    query_params = request.GET.copy()
    if 'page' in query_params:
        query_params.pop('page') 
    filters = query_params.urlencode() 

    return render(request, 'admin_panel/users/users.html', {
        'users': pages,
        'UserFilter': user_filter,
        'pages': pages,
        'filters': filters,
        })



def validate_user_role(request, form, user=None):
    new_role = form.cleaned_data['role']

    if request.user.is_superuser:
        return None

    if request.user.groups.filter(name='Agent').exists():
        if new_role == CustomUser.AGENT:
            return "You are not allowed to assign the 'Agent' role."

    elif request.user.groups.filter(name='Manager').exists():
        if new_role in [CustomUser.AGENT, CustomUser.MANAGER]:
            return "You are not allowed to assign the 'Manager' or 'Agent' roles."

    return None


@admin_only
def add_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
       
        if form.is_valid():
            error_message = validate_user_role(request, form)
            if error_message:
                messages.error(request, error_message)
                return redirect('admin_panel:users')

            new_user = form.save(commit=False)
            new_user.save()
            messages.success(request, 'The user was added successfully')
            return redirect('admin_panel:users')
    else:
        form = UserCreationForm()

    return render(request, 'admin_panel/users/add_user.html', {
        'CreateUserForm': form
    })


def validate_edit_permissions(request_user, target_user):
    current_user_group = request_user.groups.first().name if request_user.groups.exists() else None

    if request_user.is_superuser:
        return None
    
    if current_user_group == 'Agent' and target_user.role == CustomUser.AGENT:
        return "You cannot edit an Agent."
    
    elif current_user_group == 'Manager' and target_user.role in [CustomUser.AGENT, CustomUser.MANAGER]:
        return "You cannot edit an Agent or Manager."
    
    if target_user.is_superuser:
        return "You cannot edit a superuser."
    
    return None


@admin_only
def edit_user(request, uuid):

    user = CustomUser.objects.get(pk=uuid)  
     
    error_message = validate_edit_permissions(request.user, user)
    if error_message:
        messages.error(request, error_message)
        return redirect('admin_panel:users')

    
    form = EditUserForm(instance=user)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        
        if form.is_valid():
            error_message = validate_user_role(request, form, user)
            if error_message:
                messages.error(request, error_message)
                return redirect('admin_panel:users')

            user = form.save(commit=False)
            user.save()
            messages.success(request, 'The user was edited!')
            return redirect('admin_panel:users')
        
    return render(request, 'admin_panel/users/edit_user.html', {
        'EditUserForm': form,
        'user': user,
    })


@admin_only
@check_group(allowed_groups=['Agent'])
def delete_user(request, uuid):
    user = CustomUser.objects.get(pk=uuid)

    error_message = validate_edit_permissions(request.user, user)
    if error_message:
        messages.error(request, error_message)
        return redirect('admin_panel:users')

    if request.method == 'POST':
        user.delete()
        messages.success(request, 'The user was deleted successfully!')
        return redirect('admin_panel:users')
    
    return render(request, 'admin_panel/users/delete_user.html', {
        'user': user,
    })


# ===============================
# Products Management Views
# ===============================

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


# ===============================
# Categories Management Views
# ===============================


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


