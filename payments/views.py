from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
import uuid
from django.http import HttpResponse

from django.conf import settings
from orders.models import Order, OrderItem
from .models import Payment
from cart.models import Cart


def checkout(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    payment, created = Payment.objects.get_or_create(
        order=order,
        defaults={
            'amount': order.get_total_cost(),
            'currency': 'PLN',
        }
    )

    host = request.get_host()
    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': order.get_total_cost(),
        'item_name': f'Order {order.id}',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'PLN',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('payments:payment-success', kwargs={'order_id': order.id})}",
        'cancel_url': f"http://{host}{reverse('payments:payment-failed', kwargs={'order_id': order.id})}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    return render(request, 'payments/checkout.html', {
        'order': order,
        'paypal_payment': paypal_payment,
    })


def payment_successful(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    order.is_paid = True  
    order.save()

    return render(request, 'payments/payment-success.html', {
        'order': order
    })


def payment_failed(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    return render(request, 'payments/payment_failed.html', {
        'order': order
        })


def bank_transfer_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    return render(request, 'payments/bank-transfer-payment.html', {
        'order': order,
    })