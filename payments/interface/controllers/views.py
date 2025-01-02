from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.conf import settings
import uuid
from paypal.standard.forms import PayPalPaymentsForm

from orders.infrastructure.orm.models import Order
from payments.infrastructure.orm.models import Payment
from payments.application.use_cases.create_payment import CreatePayment


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


def bank_transfer_payment(request, order_id):

    order = get_object_or_404(Order, id=order_id)
    
    if request.method == "POST":
        payment_data = {
            'status': 'Pending',  
            'amount': order.get_total_cost(),
            'currency': 'PLN',
        }
        CreatePayment().execute(order, payment_data)
        return redirect('payments:payment-success', order_id=order.id)

    return render(request, 'payments/bank-transfer-payment.html', {
        'order': order,
    })


def payment_successful(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    return render(request, 'payments/payment-success.html', {
        'order': order
    })


def payment_failed(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    return render(request, 'payments/payment_failed.html', {
        'order': order,
    })
