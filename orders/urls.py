from django.urls import path
from .interface.controllers import views

app_name = 'orders'


urlpatterns = [
    path('order/', views.order_create, name='order_create'),

] 