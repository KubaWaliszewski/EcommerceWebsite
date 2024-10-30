from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from .models import Address
from orders.models import Order
from account.models import CustomUser
from .forms import UpdateUserForm, AddressForm, ChangePasswordForm


@login_required
def my_profile(request):
    
    form = UpdateUserForm(instance=request.user)

    return render(request, 'client/my-profile.html',{
        'UpdateUserForm': form,
    })



def add_address(request):

    form = AddressForm()
    
    if request.method == 'POST':
        form = AddressForm(request.POST)
        
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()

            return redirect('client:my-addresses')

    return render(request, 'client/add_address.html', {
        'AddressForm': form,
    })


def my_addresses(request):

    if request.method == 'POST':
        address_id = request.POST.get('address_id')
        address = get_object_or_404(Address, id=address_id, user=request.user)
        address.delete()
        return redirect('client:my-addresses') 


    addresses = Address.objects.filter(user=request.user)
    
    return render(request, 'client/my-addresses.html', {
        'addresses': addresses,
    })

def set_default_address(request, pk):
    address = Address.objects.get(id=pk, user=request.user)

    address.default = True
    address.save()

    return redirect('client:my-addresses')

def edit_address(request, pk):

    address = Address.objects.get(id=pk, user=request.user)
    
    form = AddressForm(instance=address)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        
        if form.is_valid():
            form.save()
            return redirect('client:my-addresses')
        

    return render(request, 'client/edit-address.html', {
        'AddressForm': form,
    })


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
    


def delete_account(request):

    delete_user = CustomUser.objects.get(email=request.user.email)
    if request.method == 'POST':
        if request.user and delete_user:
            request.user.delete()
            return redirect('account:login-view')
        

    return render(request, 'client/delete-account.html')


def my_orders(request):
    try:
        orders = Order.objects.filter(user=request.user)
    except Order.DoesNotExist:
        orders = []

    return render(request, 'client/my-orders.html', {
        'orders': orders,
    })


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if not order.user == request.user:  
        return redirect('client:my-orders')

    return render(request, 'client/order-detail.html', {
        'order': order,
    })