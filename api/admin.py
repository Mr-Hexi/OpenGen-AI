from django.contrib import admin
from .models import ChatLog

@admin.register(ChatLog)
class ChatLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'api_key', 'timestamp')
