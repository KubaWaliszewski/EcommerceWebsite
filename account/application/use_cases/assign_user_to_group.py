from django.contrib.auth.models import Group


class AssignUserToGroup:
    """Use case to assign a user to the appropriate group based on their role."""
    
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, user):
        if user.is_superuser:
            group_name = 'Agent'
            is_staff_status = True
        elif user.role == user.AGENT:
            group_name = 'Agent'
            is_staff_status = True
        elif user.role == user.MANAGER:
            group_name = 'Manager'
            is_staff_status = False
        else:
            group_name = 'Client'
            is_staff_status = False

        group, _ = Group.objects.get_or_create(name=group_name)

        user.groups.clear()
        user.groups.add(group)

        if user.is_staff != is_staff_status:
            user.is_staff = is_staff_status
            self.user_repository.save(user)

