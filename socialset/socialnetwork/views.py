from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import RetrieveUpdateDestroyAPIView ,ListAPIView, ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UserProfileViews(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserPofileSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["nickname"]

class FollowViews(ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]


class PostListViews(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['hashtag']
    permission_classes = [IsAuthenticatedOrReadOnly]

class PostDetailViews(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]




class PostLikeViews(ListCreateAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]

class CommentViews(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]

class CommentLikeViews(ListCreateAPIView):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]

class StoryViews(ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializers
    permission_classes = [IsAuthenticatedOrReadOnly]

class GroupViews(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]