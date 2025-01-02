from django.urls import path

from .interface.controllers.views.dashboard_views import admin_dashboard
from .interface.controllers.views.user_views import user_view, users, add_user, edit_user, delete_user
from .interface.controllers.views.product_views import products, add_product, edit_product
from .interface.controllers.views.order_views import order_view
from .interface.controllers.views.category_views import category


app_name = 'admin_panel'


urlpatterns = [
    path('', admin_dashboard, name='admin_dashboard'),

    path('user-view/<str:uuid>/', user_view, name='user_view'),
    path('users/', users, name='users'),
    path('add-user/', add_user, name='add_user'),
    path('edit-user/<str:uuid>/', edit_user, name='edit_user'),
    path('delete-user/<str:uuid>/', delete_user, name='delete_user'),

    path('products/', products, name='products'),
    path('add_product/', add_product, name='add_product'),
    path('edit_product/<int:pk>/', edit_product, name='edit_product'),

    path('order-view/<int:order_id>/', order_view, name='order_view'),

    path('category/', category, name='category'),

]   