from orders.infrastructure.orm.models import Order
from orders.infrastructure.orm.mappers import OrderMapper


class OrderRepository:
    def get_orders_by_user(self, user):
        orders = Order.objects.filter(user=user)
        return [OrderMapper.to_domain(order) for order in orders]


    def get_order_by_id_and_user(self, order_id, user):
        try:
            order = Order.objects.get(id=order_id, user=user)
            return order
        
        except Order.DoesNotExist:
            return None