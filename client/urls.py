from django.urls import path

from . import views


app_name = 'client'

urlpatterns = [
    # User profile
    path('', views.my_profile, name='my-profile'),
    path('add-address', views.add_address, name='add-address'),
    path('set-default-address/<int:pk>/', views.set_default_address, name='set-default-address'),
    path('my-addresses', views.my_addresses, name='my-addresses'),
    path('edit-address/<int:pk>', views.edit_address, name='edit-address'),
    path('password_change/', views.change_password, name='password_change'),
    path('delete-account', views.delete_account, name='delete-account'),
    path('my-orders', views.my_orders, name='my-orders'),
    path('order-detail/<int:order_id>', views.order_detail, name='order-detail'),

]