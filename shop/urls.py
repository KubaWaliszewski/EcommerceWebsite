from django.urls import path

from . import views


app_name = 'shop'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('category/', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<slug:category_slug>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/review/', views.add_review, name='add_review'),
]