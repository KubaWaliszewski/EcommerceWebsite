from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import send_mail
from django.conf import settings

from .token import user_tokenizer_generate
from .forms import CreateUserForm, LoginForm
from .models import CustomUser
from . import views


def register_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data.get('email')
            existing_user = CustomUser.objects.filter(email=email, is_active=False).first()
            if existing_user:
                send_verification_email(existing_user, request)


            user = form.save(commit=False)  
            user.is_active = False
            user.save()

            #Email verification config
            send_verification_email(user, request)

            return redirect('account:email-verification-sent')

        else:
            messages.error(request, 'Please correct the errors below.')

    return render(request, 'account/register.html', {
        'RegisterForm': form,
    })


def send_verification_email(user, request):

    subject = 'Active your account'
    current_site = get_current_site(request)
    message = render_to_string('account/email-verification/email-verification.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': user_tokenizer_generate.make_token(user),
    })
    user_email = user.email
    

    send_mail(subject, message, from_email=settings.EMAIL_HOST_USER, recipient_list=[user_email])


def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')

            try:
                user = authenticate(username=email, password=password)
                
                if user.check_password(password):

                    if user.is_active:
                        login(request, user)
                        return redirect('home')
                    else:
                        print('IS ACTIVE = FALSE')
                        messages.error(request, 'Account not activated.')
                        return redirect('account:resend-verification')
                else:
                    print('Email or password is incorrect')

            except:
                messages.error(request, 'Email or password is incorrect')
        else:
            messages.error(request, 'Email or password is incorrect')   

    return render(request, 'account/login.html', {
        'LoginForm': form,
    })


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


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
 

def resend_verification(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = CustomUser.objects.filter(email=email, is_active=False).first()
        if user:
            send_verification_email(user, request)
            messages.success(request, 'Verification email resent.')
            return redirect('account:email-verification-sent')
        else:
            messages.error(request, 'User does not exist or is already active.')
    return render(request, 'account/resend-verification.html')


