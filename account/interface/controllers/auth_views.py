from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from account.application.use_cases.user_registration import RegisterUserUseCase
from account.infrastructure.repositories.user_repository import UserRepository
from django.contrib import messages
from account.application.use_cases.user_login import UserLoginUseCase
from account.interface.controllers.forms import LoginForm, CreateUserForm


def register_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')

            user_repository = UserRepository()
            use_case = RegisterUserUseCase(user_repository)

            try:
                use_case.execute(email, password, first_name, last_name, request)
                return redirect('account:email-verification-sent')
            except Exception as e:
                messages.error(request, str(e))
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

            user_repository = UserRepository()
            use_case = UserLoginUseCase(user_repository)

            success, error_message = use_case.execute(request, email, password)

            if success:
                return redirect('home')
            else:
                messages.error(request, error_message)

    return render(request, 'account/login.html', {
        'LoginForm': form
    })


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')
