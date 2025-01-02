from django.shortcuts import render

from core.interface.decorators import admin_only
from orders.infrastructure.orm.models import Order
from admin_panel.application.use_cases.utils import extract_filters_from_query_params, get_filtered_and_paginated_queryset
from admin_panel.infrastructure.repositories.dashboard_repository import DashboardRepository


@admin_only
def admin_dashboard(request):

    page_number = request.GET.get('page', 1)

    paginated_users, _, user_filter, users = get_filtered_and_paginated_queryset(
        query_params=request.GET,
        repository_method=DashboardRepository.get_filtered,
        page_number=page_number,
        per_page=6
    )

    filters = extract_filters_from_query_params(request.GET)


    return render(request, 'admin_panel/dashboard.html', {
        'users': paginated_users,
        'len_users': len(users),
        'UserFilter': user_filter,
        'pages': paginated_users,
        'filters': filters,
        'orders': Order.objects.all(),
        'order_delivered': len(Order.objects.filter(status='Delivered')),
        'order_pending': len(Order.objects.filter(status='Pending')),
    })
