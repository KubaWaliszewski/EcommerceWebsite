from account.infrastructure.orm.models import CustomUser


class UserRepository:
    def get_user(uuid):
        return CustomUser.objects.get(pk=uuid)
