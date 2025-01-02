from orders.domain.entities import Order as DomainOrder, OrderItem as DomainOrderItem
from orders.infrastructure.orm.models import Order as ORMOrder, OrderItem as ORMOrderItem


class OrderMapper:
    @staticmethod
    def to_domain(orm_order: ORMOrder) -> DomainOrder:
        return DomainOrder(
            id=orm_order.id,
            user_id=orm_order.user.id if orm_order.user else None,
            full_name=orm_order.full_name,
            email=orm_order.email,
            address=orm_order.address,
            address2=orm_order.address2,
            city=orm_order.city,
            zip_code=orm_order.zip_code,
            country=orm_order.country,
            phone=orm_order.phone,
            created_at=orm_order.created_at,
            updated_at=orm_order.updated_at,
            is_paid=orm_order.is_paid,
            status=orm_order.status,
            items=[
                OrderMapper.item_to_domain(item) for item in orm_order.items.all()
            ]
        )

    @staticmethod
    def item_to_domain(orm_item: ORMOrderItem) -> DomainOrderItem:
        return DomainOrderItem(
            product_id=orm_item.product.id,
            price=float(orm_item.price),
            quantity=orm_item.quantity
        )

    @staticmethod
    def to_orm(domain_order: DomainOrder) -> ORMOrder:
        orm_order = ORMOrder(
            id=domain_order.id,
            user_id=domain_order.user_id,
            full_name=domain_order.full_name,
            email=domain_order.email,
            address=domain_order.address,
            address2=domain_order.address2,
            city=domain_order.city,
            zip_code=domain_order.zip_code,
            country=domain_order.country,
            phone=domain_order.phone,
            is_paid=domain_order.is_paid,
            status=domain_order.status,
            created_at=domain_order.created_at, 
            updated_at=domain_order.updated_at,
        )
        return orm_order
