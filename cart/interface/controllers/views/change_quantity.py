from django.shortcuts import redirect
from django.contrib import messages

from cart.application.use_cases.change_cart_item_quantity_usecase import ChangeCartItemQuantityUseCase
from cart.infrastructure.repositories.cart_repository import CartRepository


def change_quantity(request, product_id):
    action = request.GET.get('action')

    cart_repository = CartRepository()
    use_case = ChangeCartItemQuantityUseCase(cart_repository)

    success, message = use_case.execute(request.session, product_id, action)

    if not success:
        messages.error(request, message)

    return redirect('cart:cart_detail')