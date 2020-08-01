from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images', default='')
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
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField()

    def __str__(self):
        return self.body[:20]
