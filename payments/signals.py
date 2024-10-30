from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver

from .models import Payment
from orders.models import Order


@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn_obj = sender
    try:
        payment = Payment.objects.get(transaction_id=ipn_obj.invoice)
        
        if ipn_obj.payment_status == ST_PP_COMPLETED:
            order = payment.order
            order.is_paid = True
            order.save()

        elif ipn_obj.payment_status in ['Failed', 'Denied']:
            order = payment.order
            order.is_paid = False
            order.save()
    
    except Payment.DoesNotExist:
        pass