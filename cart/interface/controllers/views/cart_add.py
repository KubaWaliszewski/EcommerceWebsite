from django.views.decorators.http import require_POST
from django.http import JsonResponse

from cart.application.use_cases.add_product_to_cart_usecase import AddProductToCartUseCase
from cart.infrastructure.repositories.cart_repository import CartRepository
from shop.infrastructure.repositories.product_repository import ProductRepository


@require_POST
def cart_add(request, product_id):
    cart_repository = CartRepository()
    product_repository = ProductRepository()
    
    use_case = AddProductToCartUseCase(cart_repository, product_repository)

    success, message = use_case.execute(request.session, product_id)
    
    return JsonResponse({
        'success': success,
        'message': message,
    })