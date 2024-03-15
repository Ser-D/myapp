from django.contrib import admin

from goods.models import Categories, Products


# admin.site.register(Categories)
# admin.site.register(Products)

@admin.register(Categories)
class CategoriesAdminad(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductsAdminad(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
