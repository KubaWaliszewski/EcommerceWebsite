from django.shortcuts import render, redirect, get_object_or_404
from core.decorators import admin_only
from django.contrib import messages

from orders.models import Order


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
