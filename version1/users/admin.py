from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Admin, Customer

admin.site.register(Admin, UserAdmin)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass
