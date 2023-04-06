from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.surname}"

    def add_event(self, event) -> 'UsersEvents':
        event_content_type = ContentType.objects.get_for_model(event)

        return UsersEvents.objects.create(
            user=self,
            event_content_type=event_content_type,
            event_object_id=event.pk,
        )



class Note(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-created_at']


class Achievement(models.Model):
    title = models.CharField(max_length=100)
    reasons = models.TextField()
    icon = models.ImageField(blank=True, upload_to='images/achievements/%Y/%m/%d')

    def __str__(self):
        return f"{self.title}"




class Ad(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/ad/%Y/%m/%d')
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-created_at']


class UsersEvents(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    user = models.ForeignKey(
        User,
        models.CASCADE,
        related_name='events'
    )

    event_object_id = models.IntegerField()
    event_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT
    )
    event = GenericForeignKey(
        'event_content_type',
        'event_object_id'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"user: {self.user.name} event: {self.event.title}"
