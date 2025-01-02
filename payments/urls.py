from django.urls import path
from .interface.controllers import views


app_name = 'payments'

urlpatterns = [
    path('checkout/<int:order_id>/', views.checkout, name='checkout'),
    path('bank-transfer-payment/<int:order_id>/', views.bank_transfer_payment, name='bank-transfer-payment'),
    path('payment-success/<int:order_id>/', views.payment_successful, name='payment-success'),
    path('payment-failed/<int:order_id>/', views.payment_failed, name='payment-failed'),
]
