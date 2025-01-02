from payments.infrastructure.orm.models import Payment
from payments.domain.entities import Payment as DomainPayment
from payments.infrastructure.orm.mappers import PaymentMapper


class PaymentService:
    @staticmethod
    def process_payment(payment_data, order) -> DomainPayment:
        orm_payment, created = Payment.objects.get_or_create(
            order=order,
            defaults={
                'amount': payment_data['amount'],
                'transaction_id': payment_data.get('transaction_id'),
                'currency': payment_data.get('currency', 'PLN'),
            }
        )
        if not created:
            orm_payment.transaction_id = payment_data.get('transaction_id', orm_payment.transaction_id)
            orm_payment.amount = payment_data['amount']
            orm_payment.currency = payment_data.get('currency', 'PLN')
            orm_payment.save()

        if payment_data['status'] == 'Completed':
            PaymentService.mark_order_as_paid(order)
        elif payment_data['status'] in ['Failed', 'Denied']:
            PaymentService.mark_order_as_failed(order)

        return PaymentMapper.to_domain(orm_payment)

    @staticmethod
    def mark_order_as_paid(order):
        order.is_paid = True
        order.save()

    @staticmethod
    def mark_order_as_failed(order):
        order.is_paid = False
        order.save()
