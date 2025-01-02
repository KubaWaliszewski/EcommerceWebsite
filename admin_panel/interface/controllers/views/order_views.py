from django.shortcuts import render, redirect, get_object_or_404

from core.interface.decorators import admin_only
from orders.infrastructure.orm.models import Order
from django.contrib import messages
from admin_panel.application.use_cases.order_usecases import UpdateOrderStatusUseCase
from admin_panel.infrastructure.repositories.order_repository import OrderRepository


@admin_only
def order_view(request, order_id):
    order_repository = OrderRepository()
    use_case = UpdateOrderStatusUseCase(order_repository)

    if request.method == 'POST':
        order, status_updated = use_case.execute(request, order_id)
        
        if status_updated:
            return redirect('admin_panel:order_view', order_id=order.id)
        else:
            messages.error(request, 'Invalid status for the order.')

    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin_panel/orders/order-view.html', {
        'order': order,
    })