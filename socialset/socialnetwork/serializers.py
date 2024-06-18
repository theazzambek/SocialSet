from .models import *
from rest_framework.serializers import ModelSerializer


class UserPofileSerializers(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

class FollowSerializers(ModelSerializer):
    class Meta:
        model = Follow
        fields = "__all__"

class PostSerializers(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class PostLikeSerializers(ModelSerializer):
    class Meta:
        model = PostLike
        fields = "__all__"

class CommentsSerializers(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class CommentLikeSerializers(ModelSerializer):
    class Meta:
        model = CommentLike
        fields = "__all__"

class StorySerializers(ModelSerializer):
    class Meta:
        model = Story
        fields = "__all__"

class GroupSerializers(ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

