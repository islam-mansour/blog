from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from .models import Post, Like
from .serializers import LikeToggleSerializer
from .models import Comment
from .serializers import CommentSerializer


class LikeToggleAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = LikeToggleSerializer(data=request.data)
        if serializer.is_valid() and request.user.is_authenticated:
            post_id = serializer.validated_data['post_id']
            post = get_object_or_404(Post, id=post_id)
            user = request.user

            # Toggle like/unlike
            liked, created = Like.objects.get_or_create(post=post, user=user)
            if not created:
                liked.delete()
                return Response({'message': 'Unliked', 'likes_count': post.like_set.count()}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Liked', 'likes_count': post.like_set.count()}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from .tasks import send, receive
class CommentCreateAPI(APIView):
    
    def post(self, request, post_id):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return Response({'message': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

        # Get the associated blog
        post = get_object_or_404(Post, pk=post_id)
        
        # TODO: figure why are you having connection refused #
        # send.delay()

        # receive.delay()

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post, user=request.user)
            return Response({'message': 'Comment created successfully'}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)