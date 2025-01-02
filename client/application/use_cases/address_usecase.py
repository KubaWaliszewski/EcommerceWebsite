from client.interface.controllers.forms import AddressForm
from client.domain.entities import Address as DomainAddress


class AddAddressUseCase:
    def __init__(self, repository):
        self.repository = repository
    
    def execute(self, request):
        form = AddressForm()
        if request.method == 'POST':
            form = AddressForm(request.POST) 
            if form.is_valid():
                default = form.cleaned_data.get('default', False)
                address = DomainAddress(
                    id=None,  
                    user=request.user,  
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    address=form.cleaned_data['address'],
                    address2=form.cleaned_data.get('address2', ''),
                    city=form.cleaned_data['city'],
                    zip_code=form.cleaned_data['zip_code'],
                    country=form.cleaned_data['country'],
                    phone=form.cleaned_data['phone'],
                    default=default,
                )
                self.repository.save_address(address)
   
                return True, None
 
        return False, form


class EditAddressUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, request, address_id):
        address = self.repository.get_address_instance(address_id, request.user)

        if not address:
            return False, None

        form = AddressForm(instance=address)
        if request.method == 'POST':
            form = AddressForm(request.POST, instance=address)
            
            if form.is_valid():
                updated_address = form.save(commit=False)
                self.repository.save_address(updated_address)
                return True, None
            
        return False, form
    

class GetAddressesUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user):
        return self.repository.get_addresses_by_user(user)
    
    
class DeleteAddressUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user, address_id):
        address = self.repository.get_address_by_id_and_user(address_id, user)
        if address:
            self.repository.delete_address(address)
            return True
        return False
    

class SetDefaultAddressUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user, address_id):
        address = self.repository.get_address_by_id_and_user(address_id, user)
        if address:
            address.default = True
            self.repository.save_address(address)
            return True
        return False