from rest_framework import serializers

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=100)
    created_datetime = serializers.DateTimeField(read_only=True)
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
