from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import serializers

from .models import News, Comment

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "first_name"]

class NewsListSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ["url", "author", "title"]
        extra_kwargs = {
            'url': {'view_name': 'news_detail', 'lookup_field': 'slug'},
        }

class CommentSerializer(serializers.ModelSerializer):
    news = serializers.SlugRelatedField(slug_field="slug", queryset=News.objects.all())
    class Meta:
        model = Comment
        fields = ["news", "content"]


class NewsDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ["slug", "title", "author", "content", "comments"]

