from django.contrib import admin

from .infrastructure.orm.models import Payment

admin.site.register(Payment)