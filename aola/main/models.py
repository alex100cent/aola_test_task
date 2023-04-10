from django.db import models
from polymorphic.models import PolymorphicModel


class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    posts = models.ManyToManyField(
        'Post',
        related_name='users',
        through='UsersPosts',
    )

    def __str__(self):
        return f"{self.name} {self.surname}"


class Post(PolymorphicModel):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-created_at']


class Note(Post):
    POST_TYPE = 'note'
    body = models.TextField()

    def __str__(self):
        return f"{self.title}"


class Achievement(Post):
    POST_TYPE = 'achievement'
    body = models.TextField()

    def __str__(self):
        return f"{self.title}"


class Ad(models.Model):
    POST_TYPE = 'ad'

    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    body = models.TextField()
    url = models.URLField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-created_at']


class UsersPosts(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    users = models.ForeignKey(User, models.CASCADE)
    posts = models.ForeignKey(Post, models.CASCADE)

    class Meta:
        ordering = ['-created_at']
