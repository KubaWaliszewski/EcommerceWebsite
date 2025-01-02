from account.infrastructure.orm.models import CustomUser

def validate_user_role(request, form, user=None):
    new_role = form.cleaned_data['role']

    if request.user.is_superuser:
        return None

    if request.user.groups.filter(name='Agent').exists():
        if new_role == CustomUser.AGENT:
            return "You are not allowed to assign the 'Agent' role."

    elif request.user.groups.filter(name='Manager').exists():
        if new_role in [CustomUser.AGENT, CustomUser.MANAGER]:
            return "You are not allowed to assign the 'Manager' or 'Agent' roles."

    return None


def validate_edit_permissions(request_user, target_user):
    current_user_group = request_user.groups.first().name if request_user.groups.exists() else None

    if request_user.is_superuser:
        return None

    if current_user_group == 'Agent' and target_user.role == CustomUser.AGENT:
        return "You cannot edit an Agent."

    elif current_user_group == 'Manager' and target_user.role in [CustomUser.AGENT, CustomUser.MANAGER]:
        return "You cannot edit an Agent or Manager."

    if target_user.is_superuser:
        return "You cannot edit a superuser."

    return None
