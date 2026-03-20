from rest_framework.views import exception_handler
from rest_framework.exceptions import AuthenticationFailed, Throttled, APIException
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if response is not None:
        error_type = "invalid_request_error"
        message = "An error occurred"
        
        # Format the message depending on error type
        if isinstance(exc, AuthenticationFailed):
            error_type = "authentication_error"
            message = exc.detail
            response.status_code = status.HTTP_401_UNAUTHORIZED
        elif isinstance(exc, Throttled):
            error_type = "rate_limit_error"
            message = f"Rate limit exceeded. Try again in {exc.wait} seconds."
            response.status_code = 429
        elif isinstance(exc, APIException):
            if exc.status_code == 503:
                error_type = "server_error"
            message = str(exc)
        else:
            # For Validation errors or formatting
            message = str(exc)
            
        if isinstance(message, list) or isinstance(message, dict):
            # Fallback for complex validation responses
            message = str(response.data)
            
        response.data = {
            "error": {
                "message": message,
                "type": error_type
            }
        }
        
    return response
