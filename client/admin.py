from django.contrib import admin

from .infrastructure.orm.models import Address


admin.site.register(Address)