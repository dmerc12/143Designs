from django.utils.html import format_html
from .models import Message, Testimonial
from django.contrib import admin

# Registers messages with the admin site
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['custom_id', 'first_name', 'last_name', 'email', 'phone_number', 'title']
    view_only_fields = ['first_name', 'last_name', 'email', 'phone_number', 'title', 'message']
    list_filter = ['first_name', 'last_name', 'email', 'phone_number']
    search_fields = ['pk', 'first_name', 'last_name', 'email', 'phone_number', 'title__starts_with', 'title__contains', 'message__contains']

    # Displays a custom ID for the messages
    def custom_id(self, obj):
        return format_html(f'143DMES{obj.id}')

    # Alters column header for custom ID function above
    custom_id.short_description = 'Message Number'

# Registers testimonials with the admin site
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['custom_id', 'customer', 'featured', 'review']
    list_filter = ['customer__first_name', 'customer__last_name', 'featured']
    search_fields = ['pk', 'customer__first_name', 'customer__last_name', 'review', 'review__contains']

    # Displays a custom ID for the testimonials
    def custom_id(self, obj):
        return format_html(f'143DTES{obj.id}')

    # Alters column header for custom ID function above
    custom_id.short_description = 'Message Number'
