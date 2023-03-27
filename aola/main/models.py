from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Note(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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


class UsersAchievements(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    received_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.user.name} {self.achievement.name}"

    class Meta:
        ordering = ['-received_at']


class Ad(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/ad/%Y/%m/%d')
    url = models.URLField()
    published_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-published_at']
