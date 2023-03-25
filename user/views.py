from django.contrib.auth import get_user_model

from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from user import serializers as _
from user.permissions import AdminOrOwnerPermission

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = _.UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'phone']

    def perform_destroy(self, instance: User):
        instance.is_active = False
        instance.save()

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AdminOrOwnerPermission]
        return [permission() for permission in permission_classes]