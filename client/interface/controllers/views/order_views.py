from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from client.infrastructure.repositories.order_repository import OrderRepository
from client.application.use_cases.orders_usecase import GetOrdersUseCase, GetOrderDetailUseCase


@login_required
def my_orders(request):
    repository = OrderRepository()
    usecase = GetOrdersUseCase(repository)
    orders = usecase.execute(request.user)

    return render(request, 'client/my-orders.html', {
        'orders': orders,
    })

@login_required
def order_detail(request, order_id):
    repository = OrderRepository()
    usecase = GetOrderDetailUseCase(repository)
    order = usecase.execute(request.user, order_id)

    if not order:  
        return redirect('client:my-orders')

    return render(request, 'client/order-detail.html', {
        'order': order,
    })
