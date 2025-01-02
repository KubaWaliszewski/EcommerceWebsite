from django.contrib import messages

from .validation_helpers import validate_user_role, validate_edit_permissions
from admin_panel.interface.controllers.forms import UserCreationForm, EditUserForm
from account.infrastructure.orm.mappers import UserMapper


class GetUserDetailsUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, uuid):
        user = self.user_repository.get_user_by_id(uuid)
        if not user:
            raise ValueError("User not found")
        orders = self.user_repository.get_orders_by_user(user.id)
        return user, orders


class AddUserUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, request):
        form = UserCreationForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            error_message = validate_user_role(request, form)
            if error_message:
                messages.error(request, error_message)
                return False, form

            domain_user = form.save(commit=False)
            self.user_repository.save(domain_user)
            messages.success(request, 'The user was added successfully')
            return True, None
        return False, form


class EditUserUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, request, uuid):
        domain_user = self.user_repository.get_user_by_id(uuid)
        if not domain_user:
            return False, None, None

        error_message = validate_edit_permissions(request.user, domain_user)
        if error_message:
            messages.error(request, error_message)
            return False, None, None

        orm_user = UserMapper.to_orm(domain_user)

        form = EditUserForm(request.POST or None, instance=orm_user)

        if request.method == 'POST' and form.is_valid():
            error_message = validate_user_role(request, form, orm_user)
            if error_message:
                messages.error(request, error_message)
                return False, None, None

            updated_user = form.save(commit=False)
            self.user_repository.save(updated_user)

            messages.success(request, 'The user was edited!')
            return True, None, None

        return False, form, orm_user


class DeleteUserUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository
    
    def execute(self, request, uuid):
        user = self.user_repository.get_user_by_id(uuid)
        if not user:
            messages.error(request, "User does not exist.")
            return False, None
        
        error_message = validate_edit_permissions(request.user, user)
        if error_message:
            messages.error(request, error_message)
            return False, None

        if request.method == 'POST':
            self.user_repository.delete(user)
            messages.success(request, 'The user was deleted successfully!')
            return True, user
        return False, user
