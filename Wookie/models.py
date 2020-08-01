from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images', default='')
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
