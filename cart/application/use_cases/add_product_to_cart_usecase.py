
class AddProductToCartUseCase:
    def __init__(self, cart_repository, product_repository):
        self.cart_repository = cart_repository
        self.product_repository = product_repository

    def execute(self, session, product_id):
        cart_id = session.get('cart_id')
        cart, created = self.cart_repository.get_or_create_cart(cart_id)

        if created:
            session['cart_id'] = cart.id

        product = self.product_repository.get_by_id(product_id)


        cart_item, created = self.cart_repository.get_or_create_cart_item(cart, product)

        if not created:
            if cart_item.quantity + 1 > product.stock:
                return False, f"Insufficient stock of product {product.name}. Available: {product.stock}, in your cart: {cart_item.quantity}."
            cart_item.quantity += 1
        else:
            if product.stock < 1:
                return False, f"Insufficient stock of product {product.name}. Maximum quantity available: {product.stock}."

        self.cart_repository.save_cart_item(cart_item)

        return True, f"Added {product.name} to cart."