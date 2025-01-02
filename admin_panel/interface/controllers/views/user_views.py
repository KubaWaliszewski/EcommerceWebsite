from django.shortcuts import render, redirect
from core.interface.decorators import admin_only, check_group

from admin_panel.application.use_cases.utils import extract_filters_from_query_params, get_filtered_and_paginated_queryset
from admin_panel.infrastructure.repositories.user_repository import UserRepository

from admin_panel.application.use_cases.user_usecases import (
    GetUserDetailsUseCase,
    AddUserUseCase,
    EditUserUseCase,
    DeleteUserUseCase,
)


@admin_only
def user_view(request, uuid):
    user_repository = UserRepository()
    use_case = GetUserDetailsUseCase(user_repository)
    user, orders = use_case.execute(uuid)

    return render(request, 'admin_panel/users/user-view.html',{
        'user': user,
        'orders': orders,
    })


@admin_only
@check_group(allowed_groups=['Agent'])
def users(request):

    page_number = request.GET.get('page', 1)

    paginated_users, _, user_filter, users = get_filtered_and_paginated_queryset(
        query_params=request.GET,
        repository_method=UserRepository.get_filtered,
        page_number=page_number,
        per_page=10
    )

    filters = extract_filters_from_query_params(request.GET)

    return render(request, 'admin_panel/users/users.html', {
        'users': paginated_users,
        'UserFilter': user_filter,
        'pages': paginated_users,
        'filters': filters,
        'len_users': len(users)
        })


@admin_only
def add_user(request):
    user_repository = UserRepository()
    use_case = AddUserUseCase(user_repository)
    success, form = use_case.execute(request)
    if success:
        return redirect('admin_panel:users')

    return render(request, 'admin_panel/users/add_user.html', {
        'CreateUserForm': form,
    })


@admin_only
def edit_user(request, uuid):
    user_repository = UserRepository()
    use_case = EditUserUseCase(user_repository)
    success, form, user = use_case.execute(request, uuid)
    if user is None:
        return redirect('admin_panel:users')
    if success:
        return redirect('admin_panel:users')

    return render(request, 'admin_panel/users/edit_user.html', {
        'EditUserForm': form,
        'user': user,
    })


@admin_only
@check_group(allowed_groups=['Agent'])
def delete_user(request, uuid):
    user_repository = UserRepository()
    use_case = DeleteUserUseCase(user_repository)
    success, user = use_case.execute(request, uuid)

    if user is None:
        return redirect('admin_panel:users')
    if success:
        return redirect('admin_panel:users')

    return render(request, 'admin_panel/users/delete_user.html', {
        'user': user,
    })