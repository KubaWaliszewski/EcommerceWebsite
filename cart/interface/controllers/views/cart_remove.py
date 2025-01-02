from django.shortcuts import redirect

from cart.application.use_cases.remove_product_from_cart_usecase import RemoveProductFromCartUseCase
from cart.infrastructure.repositories.cart_repository import CartRepository


def cart_remove(request, product_id):
    cart_repository = CartRepository()
    use_case = RemoveProductFromCartUseCase(cart_repository)

    success = use_case.execute(request.session, product_id)

    return redirect('cart:cart_detail')     