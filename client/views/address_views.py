from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from client.models import Address
from client.forms import AddressForm



@login_required
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


@login_required
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


@login_required
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


@login_required
def set_default_address(request, pk):
    address = Address.objects.get(id=pk, user=request.user)

    address.default = True
    address.save()

    return redirect('client:my-addresses')
