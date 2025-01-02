from cart.domain.entities import Cart as DomainCart, CartItem as DomainCartItem
from cart.infrastructure.orm.models import Cart as ORMCart, CartItem as ORMCartItem


class CartMapper:
    @staticmethod
    def to_domain(orm_cart: ORMCart) -> DomainCart:
        """Map ORM Cart to Domain Cart."""
        items = [
            CartItemMapper.to_domain(item) for item in orm_cart.items.all()
        ]
        return DomainCart(
            id=orm_cart.id,
            created_at=orm_cart.created_at.isoformat(),
            items=items,
        )

    @staticmethod
    def to_orm(domain_cart: DomainCart) -> ORMCart:
        """Map Domain Cart to ORM Cart."""
        orm_cart = ORMCart.objects.get(pk=domain_cart.id) if domain_cart.id else ORMCart()
        orm_cart.id = domain_cart.id
        orm_cart.created_at = domain_cart.created_at
        return orm_cart


class CartItemMapper:
    @staticmethod
    def to_domain(orm_cart_item: ORMCartItem) -> DomainCartItem:
        """Map ORM CartItem to Domain CartItem."""
        return DomainCartItem(
            id=orm_cart_item.id,
            product_price=orm_cart_item.product.price,
            quantity=orm_cart_item.quantity,
            cart_id=orm_cart_item.cart.id,
            product_id=orm_cart_item.product.id,
        )

    @staticmethod
    def to_orm(domain_cart_item: DomainCartItem, orm_cart: ORMCart) -> ORMCartItem:
        orm_cart_item = ORMCartItem.objects.get(pk=domain_cart_item.id) if domain_cart_item.id else ORMCartItem()
        orm_cart_item.cart = orm_cart
        orm_cart_item.product_id = domain_cart_item.product_id
        orm_cart_item.quantity = domain_cart_item.quantity
        return orm_cart_item
