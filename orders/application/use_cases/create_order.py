class CreateOrderUseCase:
    def __init__(self, order_service, order_repository):
        self.order_service = order_service
        self.order_repository = order_repository

    def execute(self, user, form_data, cart, payment_method, request):
        if not cart.items:
            raise ValueError("Your cart is empty.")

        order = self.order_service.create_order(user, form_data, cart)

        insufficient_stock = self.order_service.check_stock(cart)
        if insufficient_stock:
            self.order_service.rollback_order(order)
            raise ValueError("Insufficient stock for one or more items.")
        
        self.order_service.add_order_items(order, cart)

        self.order_repository.save(order)

        self.order_service.reduce_stock(cart)

        self.order_service.clear_cart(cart, request)

        return order
