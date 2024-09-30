from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from django_filters.rest_framework import FilterSet, filters
from django.contrib.auth import get_user_model
from .models import Post, Comment
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
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        # Serialize the posts
        serializer = PostSerializer(posts, many=True)

        # Return the serialized data
        return Response(serializer.data)
