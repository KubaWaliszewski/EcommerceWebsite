from django.shortcuts import render, redirect
from django.contrib import messages

from account.application.use_cases.user_verification import UserVerification
from account.infrastructure.repositories.user_repository import UserRepository


def email_verification(request, uidb64, token):
    user_repository = UserRepository()

    use_case = UserVerification(user_repository)

    try:
        if use_case.execute(uidb64, token):
            return redirect('account:email-verification-success')
        else:
            messages.error(request, 'Invalid or expired verification link.')
            return redirect('account:email-verification-failed')

    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
        return redirect('account:email-verification-failed')


def email_verification_sent(request):
    return render(request, 'account/email-verification/email-verification-sent.html')


def email_verification_failed(request):
    return render(request, 'account/email-verification/email-verification-failed.html')


def email_verification_success(request):
    return render(request, 'account/email-verification/email-verification-success.html')
