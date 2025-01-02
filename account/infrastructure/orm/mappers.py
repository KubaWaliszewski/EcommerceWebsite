from account.domain.entities import DomainUser
from account.infrastructure.orm.models import CustomUser as ORMUser

class UserMapper:
    def to_domain(orm_user: ORMUser) -> DomainUser:
        """Map ORM user to domain user."""
        try:
            domain_user = DomainUser(
                id=orm_user.id,
                email=orm_user.email,
                first_name=orm_user.first_name,
                last_name=orm_user.last_name,
                role=orm_user.role,
                is_active=orm_user.is_active,
                is_staff=orm_user.is_staff,
                date_joined=orm_user.date_joined,
                last_login=orm_user.last_login,
            )
            return domain_user
        except Exception as e:
            raise


    @staticmethod
    def to_orm(domain_user: DomainUser) -> ORMUser:
        """Map domain user to ORM user."""
        try:
            if domain_user.id:
                orm_user = ORMUser.objects.get(pk=domain_user.id)
            else:
                orm_user = ORMUser()  

            orm_user.id = domain_user.id
            orm_user.email = domain_user.email
            orm_user.first_name = domain_user.first_name
            orm_user.last_name = domain_user.last_name
            orm_user.role = domain_user.role
            orm_user.is_active = domain_user.is_active
            orm_user.is_staff = domain_user.is_staff
            orm_user.date_joined = domain_user.date_joined
            orm_user.last_login = domain_user.last_login
            return orm_user
        except ORMUser.DoesNotExist:
            orm_user = ORMUser(
                id=domain_user.id,
                email=domain_user.email,
                first_name=domain_user.first_name,
                last_name=domain_user.last_name,
                role=domain_user.role,
                is_active=domain_user.is_active,
                is_staff=domain_user.is_staff,
                date_joined=domain_user.date_joined,
                last_login=domain_user.last_login,
            )
            return orm_user
        except Exception as e:
            raise