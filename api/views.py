from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import time
import uuid

from .serializers import ChatCompletionRequestSerializer
from .models import ChatLog
from services.ollama_client import generate_chat_completion, OllamaServiceError, OllamaTimeoutError, OllamaConnectionError
import requests
from django.conf import settings

class HealthCheckView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    
    def get(self, request):
        ollama_status = "unavailable"
        try:
            base_url = settings.OLLAMA_URL.replace('/api/generate', '')
            if not base_url: base_url = 'http://localhost:11434'
            res = requests.get(base_url, timeout=3)
            if res.status_code == 200:
                ollama_status = "running"
        except:
            pass
            
        return Response({
            "status": "ok",
            "ollama": ollama_status
        })

class ChatCompletionView(APIView):
    def post(self, request):
        serializer = ChatCompletionRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        messages = serializer.validated_data['messages']
        model_name = serializer.validated_data.get('model', 'phi')
        
        try:
            response_text = generate_chat_completion(messages)
        except OllamaTimeoutError as e:
            return Response(
                {"error": {"message": str(e), "type": "server_error"}},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        except OllamaConnectionError as e:
            return Response(
                {"error": {"message": str(e), "type": "service_unavailable"}},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        except OllamaServiceError as e:
            return Response(
                {"error": {"message": str(e), "type": "server_error"}},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
            
        # Log it
        ChatLog.objects.create(
            api_key=request.auth,
            prompt=str(messages),
            response=response_text
        )
            
        # Format the response
        response_data = {
            "id": f"chatcmpl-{uuid.uuid4().hex[:12]}",
            "object": "chat.completion",
            "created": int(time.time()),
            "model": "phi",
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": response_text
                    },
                    "finish_reason": "stop"
                }
            ]
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
