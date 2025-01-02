from orders.infrastructure.orm.models import Order as ORMOrder
from orders.infrastructure.orm.mappers import OrderMapper
from client.infrastructure.orm.models import Address
from client.infrastructure.orm.mappers import AddressMapper


class OrderRepository:
    def save(self, order):
        orm_order = OrderMapper.to_orm(order)
        orm_order.save()
        return OrderMapper.to_domain(orm_order)
    
    def delete(self, order):
        try:
            orm_order = ORMOrder.objects.get(id=order.id)
            orm_order.delete()
        except ORMOrder.DoesNotExist:
            raise ValueError("Order not found")

    def get_address_by_user(self, user):
        orm_address = Address.objects.filter(user=user, default=True).first()
        if orm_address:
            return AddressMapper.to_domain(orm_address)
        return None