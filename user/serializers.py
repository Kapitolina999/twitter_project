from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import CommonPasswordValidator, UserAttributeSimilarityValidator, \
    MinimumLengthValidator
from django.core.validators import RegexValidator
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8,
                                     validators=[
                                         RegexValidator(r'(?=.*[0-9])(?=.*[a-z]){8,}',
                                                        message='Invalid password')])
    password_repeat = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'birthday', 'phone', 'email', 'password', 'password_repeat']

    def validate(self, attrs):
        if attrs.get('password'):
            password = attrs['password']
            password_repeat = attrs.pop('password_repeat')

            if password != password_repeat:
                raise serializers.ValidationError('Passwords don\'t match')

        return attrs
