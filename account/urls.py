from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from . import views


app_name = 'account'

urlpatterns = [
    # Authentication
    path('login-view', views.login_view, name='login-view'),
    path('register-view', views.register_view, name='register-view'),
    path('logout-user', views.user_logout, name='logout-user'),

    # Email verification
    path('email-verification/<str:uidb64>/<str:token>/', views.email_verification, name='email-verification'),
    path('email-verification-sent', views.email_verification_sent, name='email-verification-sent'),
    path('email-verification-failed', views.email_verification_failed, name='email-verification-failed'),
    path('email-verification-success', views.email_verification_success, name='email-verification-success'),
    path('resend-verification', views.resend_verification, name='resend-verification'),

    # Reset password
    path('reset-password/', auth_views.PasswordResetView.as_view(
        template_name="account/reset-password/password-reset.html",
        email_template_name="account/reset-password/password_reset_email.html",
        success_url=reverse_lazy('account:password_reset_done'),
    ), name="reset-password"),

    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="account/reset-password/password-reset-sent.html"), name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="account/reset-password/password-reset-form.html",
        success_url=reverse_lazy('account:password_reset_complete'),
    ), name="password_reset_confirm"),

    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name="account/reset-password/password-reset-complete.html"), name="password_reset_complete"),
    
]
