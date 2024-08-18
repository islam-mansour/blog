from rest_framework import serializers

from .models import Comment


class LikeToggleSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text']
