from django.contrib import admin

from .infrastructure.orm.models import Cart, CartItem


admin.site.register(Cart)
admin.site.register(CartItem)