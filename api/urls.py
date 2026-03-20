from django.urls import path
from .views import ChatCompletionView, HealthCheckView
from authentication.views import CreateAPIKeyView

urlpatterns = [
    path('chat/completions/', ChatCompletionView.as_view(), name='chat-completions'),
    path('health/', HealthCheckView.as_view(), name='health-check'),
    path('api-keys/', CreateAPIKeyView.as_view(), name='create-api-key'),
]
