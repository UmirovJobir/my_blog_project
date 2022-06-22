from rest_framework import serializers
from .models import Post, Comment
from accounts.validators import LessThanValidator, GreaterThanValidator
from django.contrib.auth import get_user_model
User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post']

class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[LessThanValidator(3), GreaterThanValidator(130)])
    body = serializers.CharField(validators=[LessThanValidator(3), GreaterThanValidator(5000)])
    author = serializers.ReadOnlyField(source='author.username')
    #comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = CommentSerializer(many=True)


    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author', 'comments']



class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'comments']
