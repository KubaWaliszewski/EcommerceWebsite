from orders.infrastructure.orm.models import Order
from django.contrib import messages

class UpdateOrderStatusUseCase:
    
    def __init__(self, order_repository):
        self.order_repository = order_repository

    def execute(self, request, order_id):
        order = self.order_repository.get_order_by_id(order_id)
        if not order:
            messages.error(request, "Order does not exist.")
            return None, False

        new_status = request.POST.get('status')

        if new_status in dict(order.STATUS): 
            updated_order = self.order_repository.update_order_status(order, new_status)
            messages.success(request, 'The order status was updated successfully!')
            return updated_order, True      
        messages.error(request, 'Invalid status for the order.')
        return order, False