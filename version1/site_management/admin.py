from django.utils.html import format_html
from .models import Message, Testimonial
from django.contrib import admin

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['custom_id', 'name', 'email', 'phone_number', 'title']
    view_only_fields = ['name', 'email', 'phone_number', 'title', 'message']
    list_filter = ['name', 'email', 'phone_number']
    search_fields = ['pk', 'name', 'email', 'phone_number', 'title__starts_with', 'title__contains', 'message__contains']

    def custom_id(self, obj):
        return format_html(f'143DMES{obj.id}')
    
    custom_id.short_description = 'Message Number'

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['custom_id', 'customer', 'featured', 'review']
    list_filter = ['customer__first_name', 'customer__last_name', 'featured']
    search_fields = ['pk', 'customer__first_name', 'customer__last_name', 'review', 'review__contains']

    def custom_id(self, obj):
        return format_html(f'143DTES{obj.id}')
    
    custom_id.short_description = 'Message Number'
