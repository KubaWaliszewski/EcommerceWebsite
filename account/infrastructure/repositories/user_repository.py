from account.infrastructure.orm.models import CustomUser as ORMUser
from account.domain.entities import DomainUser
from account.infrastructure.orm.mappers import UserMapper


class UserRepository:
    def get_user_by_id(self, user_id) -> DomainUser:
        try:
            orm_user = ORMUser.objects.get(id=user_id)
            return UserMapper.to_domain(orm_user)
        except ORMUser.DoesNotExist:
            return None


    def get_inactive_user_by_email(self, email) -> DomainUser:
            """Get an inactive user by email and map it to the domain entity."""
            orm_user = ORMUser.objects.filter(email=email, is_active=False).first()
            return UserMapper.to_domain(orm_user) if orm_user else None
        

    def create_user(self, email, password, first_name, last_name, is_active=True) -> DomainUser:
        """Create a new user in the database and map it to the domain entity."""
        if ORMUser.objects.filter(email=email).exists():
            raise ValueError("User with this email already exists.")
        orm_user = ORMUser.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_active=is_active
        )
        return UserMapper.to_domain(orm_user)


    def save(self, domain_user: DomainUser):
        orm_user = UserMapper.to_orm(domain_user)
        orm_user.save()

        return UserMapper.to_domain(orm_user)

