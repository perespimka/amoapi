from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class UserPassResetMail(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)

class UserPassResetPassword(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password',)

class ProfileToken(serializers.ModelSerializer):
    user = UserPassResetPassword(read_only=True)
    class Meta:
        model = Profile
        fields = ('pass_reset_token', 'user')


