from django.contrib import admin

from .models import Category, Product


admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', )
    list_per_page = 4

admin.site.register(Product, ProductAdmin)