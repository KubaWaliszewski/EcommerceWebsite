from orders.infrastructure.orm.models import Order as ORMOrder
from orders.infrastructure.orm.mappers import OrderMapper

class OrderRepository:

    @staticmethod
    def get_order_by_id(order_id):
        try:
            orm_order = ORMOrder.objects.get(id=order_id)
            return OrderMapper.to_domain(orm_order)
        except ORMOrder.DoesNotExist:
            return None

    @staticmethod
    def update_order_status(order, new_status):
        orm_order = OrderMapper.to_orm(order)
        orm_order.status = new_status
        orm_order.save()
        return OrderMapper.to_domain(orm_order)
