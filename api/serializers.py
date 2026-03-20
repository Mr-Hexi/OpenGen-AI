from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    role = serializers.CharField(max_length=50)
    content = serializers.CharField(max_length=100000)

class ChatCompletionRequestSerializer(serializers.Serializer):
    messages = MessageSerializer(many=True)
    model = serializers.CharField(required=False, default="phi")
    
    def validate_messages(self, value):
        if not value:
            raise serializers.ValidationError("messages list cannot be empty.")
            
        # Basic prompt size protection
        total_length = sum(len(msg.get('content', '')) for msg in value)
        if total_length > 10000:
            raise serializers.ValidationError("Total message content exceeds maximum prompt size (10,000 chars).")
        return value
