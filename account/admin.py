from django.contrib import admin

from account.infrastructure.orm.models import CustomUser

admin.site.register(CustomUser)