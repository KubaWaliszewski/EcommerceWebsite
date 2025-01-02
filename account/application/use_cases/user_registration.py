from account.application.services.email_service import send_verification_email


class RegisterUserUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, email, password, first_name, last_name, request):
        existing_user = self.user_repository.get_inactive_user_by_email(email)
        if existing_user:
            send_verification_email(existing_user, request)
            raise Exception('Verification email sent to the existing user.')

        user = self.user_repository.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_active=False  
        )

        self.user_repository.save(user)

        send_verification_email(user, request)
