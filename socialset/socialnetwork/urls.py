from django.urls import path, include
from .views import *

urlpatterns = [
    path('userprofile/', UserProfileViews.as_view()),
    path('userprofile/<int:pk>/', UserProfileViews.as_view()),
    path('follow/', FollowViews.as_view()),
    path('follow/<int:pk>/', FollowViews.as_view()),
    path('post/', PostListViews.as_view()),
    path('post/<int:pk>/', PostDetailViews.as_view()),
    path('postlike/', PostLikeViews.as_view()),
    path('postlikes/<int:pk>/', PostLikeViews.as_view()),
    path('comment/', CommentViews.as_view()),
    path('comment/<int:pk>/', CommentViews.as_view()),
    path('commentlikes/', CommentLikeViews.as_view()),
    path('commentlikes/<int:pk>/', CommentLikeViews.as_view()),
    path('story/', StoryViews.as_view()),
    path('story/<int:pk>/', StoryViews.as_view()),
    path('group/', GroupViews.as_view()),
    path('group/<int:pk>/', GroupViews.as_view()),
]