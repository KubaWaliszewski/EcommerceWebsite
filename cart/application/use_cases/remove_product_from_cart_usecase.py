from cart.infrastructure.orm.models import Cart, CartItem


class RemoveProductFromCartUseCase:
    def __init__(self, cart_repository):
        self.cart_repository = cart_repository

    def execute(self, session, product_id):
        cart_id = session.get('cart_id')
        if not cart_id:
            return False

        try:
            cart = self.cart_repository.get_by_id(cart_id)
        except Cart.DoesNotExist:
            return False

   
        cart_item = self.cart_repository.get_cart_item_id(cart, product_id)
        if not cart_item:
            return False  

    
        self.cart_repository.delete_cart_item(cart_item)
        return True