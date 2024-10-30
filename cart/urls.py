from django.urls import path

from . import views


app_name = 'cart'


urlpatterns = [
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('change-quantity/<product_id>', views.change_quantity, name='change_quantity'),
]