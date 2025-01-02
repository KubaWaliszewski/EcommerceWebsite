from django.urls import path

from .interface.controllers.views.cart_add import cart_add
from .interface.controllers.views.cart_detail import cart_detail
from .interface.controllers.views.cart_remove import cart_remove
from .interface.controllers.views.change_quantity import change_quantity


app_name = 'cart'

urlpatterns = [
    path('cart/add/<int:product_id>/', cart_add, name='cart_add'),
    path('cart/', cart_detail, name='cart_detail'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
    path('change-quantity/<product_id>', change_quantity, name='change_quantity'),
]