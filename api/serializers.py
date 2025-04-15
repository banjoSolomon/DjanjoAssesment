from rest_framework import serializers

class ProcessRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    message = serializers.CharField(max_length=255)
