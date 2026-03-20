from django.db import models
from django.utils import timezone
from authentication.models import APIKey

class ChatLog(models.Model):
    api_key = models.ForeignKey(APIKey, on_delete=models.SET_NULL, null=True)
    prompt = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"ChatLog {self.id} at {self.timestamp}"
