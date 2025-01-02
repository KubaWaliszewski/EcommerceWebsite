class GetOrdersUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user):
        return self.repository.get_orders_by_user(user)


class GetOrderDetailUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user, order_id):
        return self.repository.get_order_by_id_and_user(order_id, user)