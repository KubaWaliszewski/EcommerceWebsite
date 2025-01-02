from django.db.models.signals import post_save
from django.dispatch import receiver
from account.infrastructure.repositories.user_repository import UserRepository
from account.application.use_cases.assign_user_to_group import AssignUserToGroup
from account.infrastructure.orm.models import CustomUser


@receiver(post_save, sender=CustomUser)
def assign_group_based_on_role(sender, instance, created, **kwargs):
    user_repository = UserRepository()
    use_case = AssignUserToGroup(user_repository)

    use_case.execute(instance)
