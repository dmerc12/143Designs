from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from .models import Admin, Customer, Supplier
from django.contrib import admin
from django import forms

# Admin creation form
class CustomAdminCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, help_text='Enter the first name of the admin.')
    last_name = forms.CharField(max_length=50, required=True, help_text='Enter the last name of the admin.')
    email = forms.EmailField(max_length=150, required=True, help_text='Enter the email of the admin.')
    
    class Meta:
        model  = Admin
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

# Creates a class for the admin users for registering in the admin site
class CustomAdminAdmin(UserAdmin):
    add_form = CustomAdminCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ['first_name', 'last_name', 'username', 'email']
    search_fields = ['first_name', 'last_name', 'username', 'email']

# Registers admin users with admin site
admin.site.register(Admin, CustomAdminAdmin)

# Registers customers with admin site
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['custom_id', 'first_name', 'last_name', 'email', 'phone_number']
    search_fields = ['id', 'first_name', 'last_name', 'email', 'phone_number']

    # Displays a custom ID for the customers
    def custom_id(self, obj):
        return f'143DCUS{obj.id}'
    
    # Alters column header for custom ID function above
    custom_id.short_description = 'Customer ID'

# Registers suppliers with admin site
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['custom_id', 'name', 'location', 'notes']
    list_filter = ['location']
    search_fields = ['id', 'name', 'location']

    # Displays a custom ID for the suppliers
    def custom_id(self, obj):
        return f'143DSUP{obj.id}'
        
    # Alters column header for custom ID function above
    custom_id.short_description = 'Supplier ID'
