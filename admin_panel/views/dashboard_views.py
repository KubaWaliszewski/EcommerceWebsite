from django.shortcuts import render
from core.decorators import admin_only
from django.core.paginator import Paginator

from account.models import CustomUser
from admin_panel.filters import UserFilter
from orders.models import Order


@admin_only
def admin_dashboard(request):
    
    #Customers panel
    users = CustomUser.objects.filter(role='client')
    len_users = len(users)
    user_filter = UserFilter(request.GET, queryset=users)
    filtered_users  = user_filter.qs

    #Paginate users (customers)
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
