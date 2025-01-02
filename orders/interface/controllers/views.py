from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

from cart.infrastructure.orm.models import Cart
from orders.application.use_cases.create_order import CreateOrderUseCase
from orders.application.services.order_service import OrderService
from orders.infrastructure.repositories.order_repository import OrderRepository
from .forms import OrderCreateForm

@login_required
def order_create(request):
    cart_id = request.session.get('cart_id')
    if not cart_id:
        return redirect('cart:cart_detail')

    cart = get_object_or_404(Cart, id=cart_id)

    if not cart or not cart.items:
        return redirect('cart:cart_detail')

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        payment_method = request.POST.get('payment_method')
        if form.is_valid():
            order_repository = OrderRepository()
            order_service = OrderService(order_repository)
            use_case = CreateOrderUseCase(order_service, order_repository)
            try:
                order = use_case.execute(
                    user=request.user,
                    form_data=form.cleaned_data,
                    cart=cart,
                    payment_method=payment_method,
                    request=request,
                )
                if payment_method == 'paypal':
                    return redirect(reverse('payments:checkout', args=[order.id]))
                elif payment_method == 'bank_transfer':
                    return redirect(reverse('payments:bank-transfer-payment', args=[order.id]))
            except ValueError as e:
                messages.error(request, str(e))
                return redirect('cart:cart_detail')

    initial_data = OrderService(OrderRepository()).get_initial_data(request.user)
    form = OrderCreateForm(initial=initial_data)

    return render(request, 'orders/order_create.html', {
        'OrderCreateForm': form,
        'cart': cart,
    })