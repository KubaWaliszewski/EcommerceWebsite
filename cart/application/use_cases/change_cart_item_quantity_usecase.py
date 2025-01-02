from cart.infrastructure.orm.models import Cart, CartItem

    
class ChangeCartItemQuantityUseCase:
    def __init__(self, cart_repository):
        self.cart_repository = cart_repository

    def execute(self, session, product_id, action):
        cart_id = session.get('cart_id')
        if not cart_id:
            return False, "Cart not found."

        cart = self.cart_repository.get_by_id(cart_id)
        if not cart:
            return False, "Cart not found."

        cart_item = self.cart_repository.get_cart_item(cart, product_id)
        if not cart_item:
            return False, "Item not found in cart."

        if action == 'increase':
            if cart_item.quantity + 1 > cart_item.product.stock:
                return False, f"Insufficient stock for product {cart_item.product.name}. Maximum available: {cart_item.product.stock}."
            cart_item.quantity += 1
        elif action == 'decrease':
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
            else:
                self.cart_repository.delete_cart_item(cart_item)
                return True, "Item removed from cart."

        self.cart_repository.save_cart_item(cart_item)
        return True, f"Quantity updated for {cart_item.product.name}."
