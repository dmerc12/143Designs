from django.contrib.auth.admin import UserAdmin
from .models import Admin, Customer, Supplier
from django.contrib import admin

admin.site.register(Admin, UserAdmin)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number']
    search_fields = ['first_name', 'last_name', 'email', 'phone_number']

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'notes']
    list_filter = ['location']
    search_fields = ['name', 'location']