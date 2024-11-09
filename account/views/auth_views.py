from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from account.services.user_services import send_verification_email

from account.forms import CreateUserForm, LoginForm
from account.models import CustomUser


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

            send_verification_email(user, request)

            return redirect('account:email-verification-sent')

        else:
            messages.error(request, 'Please correct the errors below.')

    return render(request, 'account/register.html', {
        'RegisterForm': form,
    })


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
