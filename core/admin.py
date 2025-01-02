from django.contrib import admin
from .infrastructure.orm.models import SiteConfiguration


admin.site.register(SiteConfiguration)
