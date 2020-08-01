from django.db import models

class Post1(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images', default='')
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

class Post2(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images', default='')
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

class Post3(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images', default='')
    pub_date = models.DateTimeField('date published')
    body = models.TextField()