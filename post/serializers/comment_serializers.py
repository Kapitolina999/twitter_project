from django.contrib.auth import get_user_model
from rest_framework import serializers

from post.models import Comment

User = get_user_model()


class CommentCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['date_created', 'date_updated']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        exclude = ['id', 'post']
        read_only_fields = ['date_created', 'date_updated']

