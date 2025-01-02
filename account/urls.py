from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from .interface.controllers.auth_views import login_view, register_view, user_logout
from .interface.controllers.verification_views import (
    email_verification, 
    email_verification_sent, 
    email_verification_failed, 
    email_verification_success, 
)


app_name = 'account'

urlpatterns = [
    # Authentication
    path('login-view', login_view, name='login-view'),
    path('register-view', register_view, name='register-view'),
    path('logout-user', user_logout, name='logout-user'),

    # Email verification
    path('email-verification/<str:uidb64>/<str:token>/', email_verification, name='email-verification'),
    path('email-verification-sent', email_verification_sent, name='email-verification-sent'),
    path('email-verification-failed', email_verification_failed, name='email-verification-failed'),
    path('email-verification-success', email_verification_success, name='email-verification-success'),

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
