from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status, generics
from django_filters.rest_framework import FilterSet, filters
from django.contrib.auth import get_user_model
from notifications.models import Notification
from .models import Like, Post, Comment
from .serializers import PostSerializer, CommentSerializer

User = get_user_model()


class PostFilter(FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['title']


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = PostFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)


class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get users that the current user is following
        following_users = request.user.following.all()

        # Check if following_users exists and is not empty
        if not following_users.exists():
            return Response({"detail": "You are not following anyone yet."}, status=200)

        # Get posts from the followed users, ordered by creation time
        posts = Post.objects.filter(
            author__in=following_users).order_by('-created_at')

        # Serialize the posts
        serializer = PostSerializer(posts, many=True)

        # Return the serialized data
        return Response(serializer.data)


class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Safely get the post or return 404 if not found
        post = get_object_or_404(Post, pk=pk)

        # Use Like.objects.get_or_create to handle liking the post
        like, created = Like.objects.get_or_create(
            user=request.user, post=post)

        if created:
            # If a like was successfully created, generate a notification
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked',
                target=post
            )
            return Response({'message': 'Post liked'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'You have already liked this post'}, status=status.HTTP_400_BAD_REQUEST)


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Safely get the post or return 404 if not found
        post = get_object_or_404(Post, pk=pk)

        try:
            # Attempt to get the like instance and delete it
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({'message': 'Post unliked'}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({'message': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)
