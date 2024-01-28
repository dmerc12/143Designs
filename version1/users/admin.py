from django.contrib.auth.admin import UserAdmin
from .models import Admin, Customer, Supplier
from django.contrib import admin

admin.site.register(Admin, UserAdmin)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass
