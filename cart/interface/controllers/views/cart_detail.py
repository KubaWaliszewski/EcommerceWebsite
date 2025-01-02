from django.shortcuts import render
from cart.infrastructure.repositories.cart_repository import CartRepository

def cart_detail(request):
    cart_repository = CartRepository()
    cart_id = request.session.get('cart_id')
    cart = cart_repository.get_by_id(cart_id) if cart_id else None

    return render(request, 'cart/cart.html', {
        'cart': cart,
    })
