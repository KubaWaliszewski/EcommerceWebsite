from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from client.forms import UpdateUserForm, ChangePasswordForm
from account.models import CustomUser


@login_required
def my_profile(request):
    
    form = UpdateUserForm(instance=request.user)

    return render(request, 'client/my-profile.html',{
        'UpdateUserForm': form,
    })


@login_required
def change_password(request):

    form = ChangePasswordForm(request.user)

    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()  
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password was successfully updated!')

            return redirect('client:my-profile')  
        
        else:
            messages.error(request, 'Please correct the error below.')

    return render(request, 'client/change-password.html', {
        'form': form,
    })    
    

@login_required
def delete_account(request):

    delete_user = CustomUser.objects.get(email=request.user.email)
    if request.method == 'POST':
        if request.user and delete_user:
            request.user.delete()
            return redirect('account:login-view')
        

    return render(request, 'client/delete-account.html')
