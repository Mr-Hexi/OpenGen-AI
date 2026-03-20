from rest_framework.throttling import SimpleRateThrottle

class APIKeyRateThrottle(SimpleRateThrottle):
    scope = 'api_key'
    
    def get_cache_key(self, request, view):
        if request.auth: # request.auth will be the APIKey object
            return self.cache_format % {
                'scope': self.scope,
                'ident': request.auth.key_hash
            }
        return None
