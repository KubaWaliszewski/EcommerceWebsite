from account.infrastructure.orm.models import CustomUser
from account.infrastructure.orm.mappers import UserMapper


class UserRepository:
    def get_user_by_email(self, email):
        try:
            orm_user = CustomUser.objects.get(email=email)
            return UserMapper.to_domain(orm_user) 
        except CustomUser.DoesNotExist:
            return None

    def update_user(self, user, data):
        try:
            orm_user = CustomUser.objects.get(id=user.id)
            for attr, value in data.items():
                setattr(orm_user, attr, value)
            orm_user.save()
            return UserMapper.to_domain(orm_user)  
        except CustomUser.DoesNotExist:
            return None

    def delete_user(self, user):
        try:
            orm_user = CustomUser.objects.get(id=user.id)
            orm_user.delete()
        except CustomUser.DoesNotExist:
            pass
