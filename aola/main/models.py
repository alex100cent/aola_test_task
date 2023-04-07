from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.surname}"

    def add_post(self, post) -> 'UsersPosts':
        post_content_type = ContentType.objects.get_for_model(post)

        return UsersPosts.objects.create(
            user=self,
            post_content_type=post_content_type,
            post_object_id=post.pk,
        )


class Feed(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    post_record = GenericRelation(
        'UsersPosts',
        'post_object_id',
        'post_content_type',
        related_query_name='posts'
    )


class Note(Feed):
    body = models.TextField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-created_at']


class Achievement(Feed):
    body = models.TextField()
    icon = models.ImageField(blank=True, upload_to='images/achievements/%Y/%m/%d')

    def __str__(self):
        return f"{self.title}"


class Ad(Feed):
    body = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/ad/%Y/%m/%d')
    url = models.URLField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-created_at']


class UsersPosts(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    user = models.ForeignKey(
        User,
        models.CASCADE,
        related_name='posts'
    )

    post_object_id = models.IntegerField()
    post_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT
    )
    post = GenericForeignKey(
        'post_content_type',
        'post_object_id'
    )

    class Meta:
        ordering = ['-created_at']

    # def __str__(self):
    #     return f"user: {self.user.name} event: {self.event.title}"
