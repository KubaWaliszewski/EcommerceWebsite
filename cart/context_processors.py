from .models import Cart


def cart_total_items(request):
    cart_id = request.session.get('cart_id')

    if cart_id:
        cart = Cart.objects.filter(id=cart_id).first()
        if cart:
            return {'cart_total_items': cart.get_total_quantity()}
        

    return {'cart_total_items':0}
