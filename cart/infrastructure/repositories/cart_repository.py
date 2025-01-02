from cart.infrastructure.orm.models import Cart as ORMCart, CartItem as ORMCartItem
from cart.infrastructure.orm.mappers import CartMapper, CartItemMapper


class CartRepository:
    def get_or_create_cart(self, cart_id):
        orm_cart = ORMCart.objects.get_or_create(id=cart_id)
        return orm_cart


    def save_cart_item(self, domain_cart):
        domain_cart.save()


    def get_by_id(self, cart_id):
        orm_cart = ORMCart.objects.get(id=cart_id)
        return orm_cart


    def get_or_create_cart_item(self, domain_cart, product):
        return ORMCartItem.objects.get_or_create(cart=domain_cart, product=product)


    def get_cart_item(self, domain_cart, product_id):
        return ORMCartItem.objects.get(cart=domain_cart, product_id=product_id)


    def get_cart_item_id(self, cart, product_id):
        return ORMCartItem.objects.get(cart=cart, id=product_id)


    def delete_cart_item(self, domain_cart_item):
        domain_cart_item.delete()


    def save_cart_item(self, domain_cart_item):
        domain_cart_item.save()
