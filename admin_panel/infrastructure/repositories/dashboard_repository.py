from account.infrastructure.orm.models import CustomUser

class DashboardRepository:
    
    def get_filtered(query_params):
        from admin_panel.infrastructure.filters.user_filters import UserFilter
        
        users = CustomUser.objects.filter(role='client')
        applied_filter = UserFilter(query_params, queryset=users)
        return applied_filter.qs, applied_filter, users