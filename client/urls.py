from django.urls import path

from .interface.controllers.views.profile_views import my_profile, change_password, delete_account
from .interface.controllers.views.order_views import my_orders, order_detail
from .interface.controllers.views.address_views import add_address, set_default_address, my_addresses, edit_address


app_name = 'client'

urlpatterns = [
    path('', my_profile, name='my-profile'),
    path('password_change/', change_password, name='password_change'),
    path('delete-account', delete_account, name='delete-account'),

    path('add-address', add_address, name='add-address'),
    path('set-default-address/<int:pk>/', set_default_address, name='set-default-address'),
    path('my-addresses', my_addresses, name='my-addresses'),
    path('edit-address/<int:pk>', edit_address, name='edit-address'),
    
    path('my-orders', my_orders, name='my-orders'),
    path('order-detail/<int:order_id>', order_detail, name='order-detail'),

]