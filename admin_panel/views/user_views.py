from django.shortcuts import render, redirect, get_object_or_404
from core.decorators import admin_only, check_group
from django.contrib import messages
from django.core.paginator import Paginator

from account.models import CustomUser
from admin_panel.forms import UserCreationForm, EditUserForm
from admin_panel.filters import UserFilter
from orders.models import Order


@admin_only
def user_view(request, uuid):
    user = get_object_or_404(CustomUser, id=uuid)

    orders = Order.objects.filter(user=user)

    return render(request, 'admin_panel/users/user-view.html',{
        'user': user,
        'orders': orders,
    })


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