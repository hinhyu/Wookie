from django.db import models
from django.utils import timezone
import accounts.models

class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images', default='')
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(accounts.models.Profile, on_delete=models.CASCADE, related_name="author")
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField()

    def __str__(self):
        return self.body[:20]

class Message(models.Model):
    sender = models.ForeignKey(accounts.models.Profile, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(accounts.models.Profile, on_delete=models.CASCADE, related_name="receiver")
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text[:20]