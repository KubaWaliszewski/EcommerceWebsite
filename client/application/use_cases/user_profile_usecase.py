from django.contrib.auth import update_session_auth_hash

class UpdateUserProfileUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user, data):
        return self.repository.update_user(user, data)
    

class ChangeUserPasswordUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, request, form):
        if form.is_valid():
            updated_user = form.save()
            update_session_auth_hash(request, updated_user)  
            return True, updated_user
        return False, None


class DeleteUserAccountUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user):
        self.repository.delete_user(user)
        return True