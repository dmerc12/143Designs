from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from .models import Admin, Customer, Supplier
from django.contrib import admin
from django import forms

class CustomAdminCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, help_text='Enter the first name of the admin.')
    last_name = forms.CharField(max_length=50, required=True, help_text='Enter the last name of the admin.')
    email = forms.EmailField(max_length=150, required=True, help_text='Enter the email of the admin.')
    
    class Meta:
        model  = Admin
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class CustomAdminAdmin(UserAdmin):
    add_form = CustomAdminCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ['first_name', 'last_name', 'username', 'email', 'date_joined']
    list_filter = ['date_joined',]
    search_fields = ['first_name', 'last_name', 'username', 'email', 'date_joined']

admin.site.register(Admin, CustomAdminAdmin)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number']
    search_fields = ['first_name', 'last_name', 'email', 'phone_number']

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'notes']
    list_filter = ['location']
    search_fields = ['name', 'location']
