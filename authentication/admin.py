from django.contrib import admin
from .models import APIKey

@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'is_active')
    search_fields = ('key_hash',)
    list_filter = ('is_active',)
