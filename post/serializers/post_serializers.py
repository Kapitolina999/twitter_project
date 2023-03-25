from rest_framework import serializers

from post.models import Post
from post.serializers.comment_serializers import CommentSerializer
from twitter_project.settings import NOT_VALID_TITLE_POST, USER_MIN_AGE


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get('title'):
            for word in NOT_VALID_TITLE_POST:
                if word in attrs['title'].lower():
                    raise serializers.ValidationError('Title not valid')
        return attrs


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get('title'):
            for word in NOT_VALID_TITLE_POST:
                if word in attrs['title'].lower():
                    raise serializers.ValidationError('Title not valid')

        if attrs.get('author').age < USER_MIN_AGE:
            raise serializers.ValidationError('Invalid author age')

        return attrs
