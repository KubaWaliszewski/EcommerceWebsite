from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from client.interface.controllers.forms import UpdateUserForm, ChangePasswordForm
from client.infrastructure.repositories.user_repository import UserRepository
from client.application.use_cases.user_profile_usecase import (
    UpdateUserProfileUseCase,
    ChangeUserPasswordUseCase,
    DeleteUserAccountUseCase
)


@login_required
def my_profile(request):
    repository = UserRepository()
    form = UpdateUserForm(instance=request.user)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            usecase = UpdateUserProfileUseCase(repository)
            usecase.execute(request.user, form.cleaned_data)
            messages.success(request, 'Profile updated successfully!')

    return render(request, 'client/my-profile.html', {
        'UpdateUserForm': form,
    })

    
@login_required
def change_password(request):
    repository = UserRepository()
    form = ChangePasswordForm(request.user)

    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        usecase = ChangeUserPasswordUseCase(repository)
        success, _ = usecase.execute(request, form)

        if success:
            messages.success(request, 'Your password was successfully updated!')
            return redirect('client:my-profile')
        else:
            messages.error(request, 'Please correct the error below.')

    return render(request, 'client/change-password.html', {
        'form': form,
    })
 

@login_required
def delete_account(request):
    repository = UserRepository()
    if request.method == 'POST':
        usecase = DeleteUserAccountUseCase(repository)
        success = usecase.execute(request.user)

        if success:
            messages.success(request, 'Your account has been deleted.')
            return redirect('account:login-view')

    return render(request, 'client/delete-account.html')