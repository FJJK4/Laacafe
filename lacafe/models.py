from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cat/')
    slug = models.SlugField(unique=True)


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='post/img/')
    text = models.TextField()
    video = models.FileField(upload_to='post/video/')
