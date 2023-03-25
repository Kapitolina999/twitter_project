from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from post.models import Comment
from post.permissions import AdminOrOwnerPermission
from post.serializers import comment_serializers as _


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return _.CommentCreateSerializer
        return _.CommentSerializer

    # def get_permissions(self):
    #     if self.action == 'create':
    #         permission_classes = [IsAuthenticated]
    #     elif self.action in ['list', 'retrieve']:
    #         permission_classes = [AllowAny]
    #     else:
    #         permission_classes = [AdminOrOwnerPermission]
    #     return [permission() for permission in permission_classes]