from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import APIKey, hash_api_key

class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        
        if not auth_header:
            return None
            
        if not auth_header.startswith('Bearer '):
            return None
            
        raw_key = auth_header.split(' ')[1]
        key_hash = hash_api_key(raw_key)
        
        try:
            api_key = APIKey.objects.get(key_hash=key_hash, is_active=True)
        except APIKey.DoesNotExist:
            raise AuthenticationFailed("Invalid API key")
            
        return (None, api_key)
