from rest_framework import generics, permissions
from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from notifications.models import Notification
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404




class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends =  [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        followed_users = user.following.all()
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')
        #Post.objects.filter(author__in=following_users).order_by


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, post_id):
    try:
        post = get_object_or_404(Post, id=post_id)
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if created:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post
            )
            return Response({'status': 'success', 'message': 'Post liked.'}, status=status.HTTP_200_OK)
        return Response({'status': 'error', 'message': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)
    except Post.DoesNotExist:
        return Response({'status': 'error', 'message': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, post_id):
    try:
        post = get_object_or_404(Post, id=post_id)
        like = Like.objects.filter(post=post, user=request.user)
        if like.exists():
            like.delete()
            return Response({'status': 'success', 'message': 'Post unliked.'}, status=status.HTTP_200_OK)
    except Post.DoesNotExist:
        return Response({'status': 'error', 'message': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)
