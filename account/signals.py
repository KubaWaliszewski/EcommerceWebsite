from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def assign_group_based_on_role(sender, instance, created, **kwargs):
    
    if instance.is_superuser:
        group_name = 'Agent'
        is_staff_status = True
    elif instance.role == CustomUser.AGENT:
        group_name = 'Agent'
        is_staff_status = True 
    elif instance.role == CustomUser.MANAGER:
        group_name = 'Manager'
        is_staff_status = False  
    else:
        group_name = 'Client'
        is_staff_status = False 

    group, _ = Group.objects.get_or_create(name=group_name)


    instance.groups.clear()
    instance.groups.add(group)
    

    if instance.is_staff != is_staff_status:
        instance.is_staff = is_staff_status

        post_save.disconnect(assign_group_based_on_role, sender=CustomUser)
        instance.save()
        post_save.connect(assign_group_based_on_role, sender=CustomUser)
    

