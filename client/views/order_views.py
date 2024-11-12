from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from orders.models import Order


@login_required
def my_orders(request):
    try:
        orders = Order.objects.filter(user=request.user)
    except Order.DoesNotExist:
        orders = []

    return render(request, 'client/my-orders.html', {
        'orders': orders,
    })


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if not order.user == request.user:  
        return redirect('client:my-orders')

    return render(request, 'client/order-detail.html', {
        'order': order,
    })