from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ['author', 'post', 'content', 'created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'comments', 'created_at', 'updated_at']