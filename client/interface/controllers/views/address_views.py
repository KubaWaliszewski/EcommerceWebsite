from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from client.infrastructure.repositories.address_repository import AddressRepository
from client.application.use_cases.address_usecase import (
    AddAddressUseCase, 
    EditAddressUseCase, 
    DeleteAddressUseCase, 
    GetAddressesUseCase, 
    SetDefaultAddressUseCase
)


@login_required
def add_address(request):
    repository = AddressRepository()
    usecase = AddAddressUseCase(repository)

    success, form = usecase.execute(request)

    if success:
        return redirect('client:my-addresses') 

    return render(request, 'client/add_address.html', {
        'AddressForm': form
    })


@login_required
def edit_address(request, pk):
    repository = AddressRepository()
    usecase = EditAddressUseCase(repository)

    success, form = usecase.execute(request, pk)

    if success:
        return redirect('client:my-addresses') 

    return render(request, 'client/edit-address.html', {
        'AddressForm': form,
    })


@login_required
def my_addresses(request):
    repository = AddressRepository()

    if request.method == 'POST':
        usecase = DeleteAddressUseCase(repository)
        address_id = request.POST.get('address_id')
        success = usecase.execute(request.user, address_id)
        if success:
            return redirect('client:my-addresses')

    usecase = GetAddressesUseCase(repository)

    addresses = usecase.execute(request.user)

    return render(request, 'client/my-addresses.html', {
        'addresses': addresses,
    })


@login_required
def set_default_address(request, pk):
    repository = AddressRepository()
    usecase = SetDefaultAddressUseCase(repository)

    success = usecase.execute(request.user, pk)
    if success:
        return redirect('client:my-addresses')

    return redirect('client:my-addresses')