from django.contrib.auth import authenticate, login


class UserLoginUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, request, email, password):
    
        user = authenticate(request, username=email, password=password)
        if user:
            if user.check_password(password):
                if user.is_active:
                    login(request, user)
                    return True, None  
                elif user:
                    return False, 'Account not activated.'
            else:
                return False, 'Email or password is incorrect.'
        else:
            return False, 'Email or password is incorrect.'