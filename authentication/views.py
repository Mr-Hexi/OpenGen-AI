import secrets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .models import APIKey, hash_api_key

class CreateAPIKeyView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    
    def post(self, request):
        admin_key = request.headers.get('x-admin-key')
        
        if admin_key != getattr(settings, 'ADMIN_SECRET_KEY', 'default-admin-secret-replace-me'):
            return Response(
                {"error": {"message": "Invalid admin key", "type": "authentication_error"}},
                status=status.HTTP_401_UNAUTHORIZED
            )
            
        raw_key = f"sk-opengen-{secrets.token_urlsafe(32)}"
        key_hash = hash_api_key(raw_key)
        
        APIKey.objects.create(key_hash=key_hash)
        
        return Response({"api_key": raw_key}, status=status.HTTP_201_CREATED)
