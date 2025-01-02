from payments.infrastructure.orm.models import Payment as ORMPayment
from payments.domain.entities import Payment as DomainPayment
from orders.infrastructure.orm.models import Order


class PaymentMapper:
    @staticmethod
    def to_domain(orm_payment: ORMPayment) -> DomainPayment:
        return DomainPayment(
            id=orm_payment.id,
            order_id=orm_payment.order.id if orm_payment.order else None,
            transaction_id=orm_payment.transaction_id,
            amount=float(orm_payment.amount),
            currency=orm_payment.currency,
            created_at=orm_payment.created_at,
            updated_at=orm_payment.updated_at,
            status="Completed" if orm_payment.order.is_paid else "Pending",
        )

    @staticmethod
    def to_orm(domain_payment: DomainPayment, order: Order) -> ORMPayment:
        return ORMPayment(
            id=domain_payment.id,
            order=order,
            transaction_id=domain_payment.transaction_id,
            amount=domain_payment.amount,
            currency=domain_payment.currency,
        )
