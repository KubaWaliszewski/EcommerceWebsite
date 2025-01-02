from django.urls import path

from .interface.controllers.views.search_views import search_view
from .interface.controllers.views.product_views import product_list, product_detail
from .interface.controllers.views.review_views import add_review


app_name = 'shop'

urlpatterns = [
    path('search/', search_view, name='search'),
    path('category/', product_list, name='product_list'),
    path('category/<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),
    path('product/<int:product_id>/review/', add_review, name='add_review'),
]