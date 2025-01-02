from orders.infrastructure.orm.models import Order, OrderItem
from client.infrastructure.orm.models import Address
from django.db import transaction


class OrderService:
    def __init__(self, order_repository):
        self.order_repository = order_repository

    def create_order(self, user, form_data, cart):
        order = Order.objects.create(
            user=user if user.is_authenticated else None,
            full_name=form_data['full_name'],
            email=user.email if user.is_authenticated else form_data['email'],
            address=form_data['address'],
            address2=form_data.get('address2'),
            city=form_data['city'],
            zip_code=form_data['zip_code'],
            country=form_data['country'],
            phone=form_data['phone'],
            is_paid=False
        )
        return order

    def check_stock(self, cart):
        for item in cart.items.all():
            if item.quantity > item.product.stock:
                return True
        return False

    def rollback_order(self, order):
        self.order_repository.delete(order)

    def add_order_items(self, order, cart):
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity
            )

    def reduce_stock(self, cart):
        for item in cart.items.all():
            product = item.product
            product.stock -= item.quantity
            if product.stock <= 0:
                product.is_available = False
            product.save()

    def clear_cart(self, cart, request):
        cart.delete()
        if 'cart_id' in request.session:
            del request.session['cart_id']

    def get_initial_data(self, user):
        if user.is_authenticated:
            address = self.order_repository.get_address_by_user(user)
            if address:
                return {
                    'full_name': f"{address.first_name} {address.last_name}",
                    'address': address.address,
                    'address2': address.address2,
                    'city': address.city,
                    'zip_code': address.zip_code,
                    'country': address.country,
                    'phone': address.phone,
                }
        return {}

