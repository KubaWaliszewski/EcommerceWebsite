from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from account.infrastructure.orm.models import CustomUser
from account.infrastructure.tokens import user_tokenizer_generate


class UserVerification:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, uidb64, token):
        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = self.user_repository.get_user_by_id(user_id)
            
            if user and user_tokenizer_generate.check_token(user, token):
                    if not user.is_active:
                        user.is_active = True
                        self.user_repository.save(user)
                    return True

        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            pass

        return False