from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from post.models import Post
from post.permissions import AdminOrOwnerPermission
from post.serializers import post_serializers as _


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            return _.PostCreateSerializer
        return _.PostSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [AdminOrOwnerPermission]
        return [permission() for permission in permission_classes]
