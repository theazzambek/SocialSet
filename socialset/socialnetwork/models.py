from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    nickname = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(verbose_name="Биография")
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    website = models.URLField(verbose_name="Веб-сайт", null=True, blank=True)
    followers = models.IntegerField(null=True, blank=True, default=0)

class Follow(models.Model):
    follower = models.ManyToManyField(UserProfile, verbose_name="Подписки", related_name="follower")
    following = models.ManyToManyField(UserProfile, verbose_name="Подписчики", related_name="following")
    created_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(null=True, blank=True, default=0)
    hashtag = models.CharField(max_length=32)


class PostLike(models.Model):
    user = models.ManyToManyField(UserProfile)
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    user = models.ManyToManyField(UserProfile)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    likes = models


class CommentLike(models.Model):
    user = models.ManyToManyField(UserProfile)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

class Story(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    video = models.FileField(upload_to="videos/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField(null=True, blank=True)


class Group(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="creator")
    members = models.ManyToManyField(UserProfile)
    join_key = models.CharField(max_length=64, null=True, blank=True)

