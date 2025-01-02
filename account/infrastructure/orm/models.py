import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    AGENT = 'agent'
    MANAGER = 'manager'
    CLIENT = 'client'

    ROLES_CHOICES = (
        (AGENT, 'Agent'),
        (MANAGER, 'Manager'),
        (CLIENT, 'Client'),
    )
      
    username = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLES_CHOICES, default=CLIENT)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()     
    def __str__(self):
        return self.email   

    def name(self):
        return f"{self.first_name} {self.last_name}"
