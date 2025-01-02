from django.contrib import admin

from .infrastructure.orm.models import Category, Product, Review


admin.site.register(Category)
admin.site.register(Review)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', )
    list_per_page = 4

admin.site.register(Product, ProductAdmin)