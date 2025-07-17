from rest_framework import serializers

class OpenAISerializer(serializers.Serializer):
    prompt = serializers.CharField()