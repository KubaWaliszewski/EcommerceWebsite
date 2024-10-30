from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Product

@receiver(pre_save, sender=Product)
def update_is_available(sender, instance, **kwargs):
    if instance.stock <= 0:
        instance.is_available = False
    else:
        instance.is_available = True