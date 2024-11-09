from django.shortcuts import render, redirect
from django.contrib import messages

from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from account.token import user_tokenizer_generate
from account.models import CustomUser


def email_verification(request, uidb64, token):

    try:
        unique_token = force_str(urlsafe_base64_decode(uidb64))
        custom_user = CustomUser.objects.get(pk=unique_token)

        if custom_user and user_tokenizer_generate.check_token(custom_user, token):

            custom_user.is_active = True
            custom_user.save()

            return redirect('account:email-verification-success')
        
        else:
            messages.error(request, 'Invalid or expired verification link.')
            return redirect('account:email-verification-failed')
    
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        messages.error(request, 'Invalid verification link.')
        return redirect('account:email-verification-failed')
    
 
def email_verification_sent(request):
    return render(request, 'account/email-verification/email-verification-sent.html')
 
def email_verification_failed(request):
    return render(request, 'account/email-verification/email-verification-failed.html')
 
def email_verification_success(request):
    return render(request, 'account/email-verification/email-verification-success.html')
