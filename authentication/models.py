from django.db import models
from django.utils import timezone
import hashlib

def hash_api_key(raw_key):
    return hashlib.sha256(raw_key.encode()).hexdigest()

class APIKey(models.Model):
    key_hash = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"APIKey created at {self.created_at}"
