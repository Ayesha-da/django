from django.contrib import admin
from djangoProject1.models import User, Product

#admin.site.register(User)
#admin.site.register(Product)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'name']
    list_display = ['id','username', 'email']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'description','stock']
    list_display = ['id', 'name', 'price']
    search_fields = ['id']