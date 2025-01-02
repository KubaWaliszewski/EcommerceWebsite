from account.infrastructure.orm.models import CustomUser as ORMUser
from account.domain.entities import DomainUser
from account.infrastructure.orm.mappers import UserMapper
from orders.infrastructure.orm.models import Order


class UserRepository:
    def get_filtered(query_params):
        from admin_panel.infrastructure.filters.user_filters import UserFilter
        
        users = ORMUser.objects.all()
        applied_filter = UserFilter(query_params, queryset=users)
        return applied_filter.qs, applied_filter, users
    
    def get_user_by_id(self, user_id) -> DomainUser:
        try:
            orm_user = ORMUser.objects.get(id=user_id)
            return UserMapper.to_domain(orm_user)
        except ORMUser.DoesNotExist:
            return None

    def get_orders_by_user(self, user_id):
        return Order.objects.filter(user_id=user_id)

    def save(self, domain_user: DomainUser):
        orm_user = UserMapper.to_orm(domain_user)
        orm_user.save()

    def delete(self, domain_user: DomainUser):
        orm_user = UserMapper.to_orm(domain_user)
        orm_user.delete()

   