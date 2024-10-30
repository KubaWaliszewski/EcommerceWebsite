from django.urls import path

from . import views


app_name = 'admin_panel'


urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('users/', views.users, name='users'),
    path('add-user/', views.add_user, name='add_user'),
    path('edit-user/<str:uuid>/', views.edit_user, name='edit_user'),
    path('delete-user/<str:uuid>/', views.delete_user, name='delete_user'),

    path('user-view/<str:uuid>/', views.user_view, name='user_view'),
    path('order-view/<int:order_id>/', views.order_view, name='order_view'),

    path('products/', views.products, name='products'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),

    path('category/', views.category, name='category'),

    
]   