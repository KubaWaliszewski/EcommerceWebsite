from payments.application.services.payment_service import PaymentService
from payments.infrastructure.orm.mappers import PaymentMapper


class CreatePayment:
    def execute(self, order, payment_data):
        payment_service = PaymentService()
        domain_payment = payment_service.process_payment(payment_data, order)
        orm_payment = PaymentMapper.to_orm(domain_payment, order)
        orm_payment.save()
        return PaymentMapper.to_domain(orm_payment)
