from django.core.management.base import BaseCommand
import secrets
from authentication.models import APIKey, hash_api_key

class Command(BaseCommand):
    help = 'Generates a new API Key for OpenGen AI'

    def handle(self, *args, **kwargs):
        raw_key = f"sk-opengen-{secrets.token_urlsafe(32)}"
        key_hash = hash_api_key(raw_key)
        
        APIKey.objects.create(key_hash=key_hash)
        
        self.stdout.write(self.style.SUCCESS('Successfully created new API Key!'))
        self.stdout.write(self.style.WARNING('Please save this key now. It will not be shown again.'))
        self.stdout.write(self.style.SUCCESS(f'API Key: {raw_key}'))
