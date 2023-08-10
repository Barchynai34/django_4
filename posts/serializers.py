from rest_framework import serializers
from posts.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "category", "created"]


class PostDetailSerializer(serializers.ModelSerializer):
    post_comment = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ["id", "title", "category", "created", "status", "cover", "content", "post_comment"]