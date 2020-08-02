from django.db import models
from django.utils import timezone
import accounts.models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Post(models.Model):
    title = models.CharField(max_length=150)
    image = ProcessedImageField(upload_to='images/', processors=[ResizeToFill(200, 200)], format='JPEG', options={'quality':80},)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    
    completion = (
		('beauty', 'Beauty'),
        ('art', 'Art'),
        ('other', 'Other'),
    )
    category = models.CharField(max_length=10, choices=completion, default="beauty")

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
