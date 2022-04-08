from django.db import models

from django.conf import settings
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts", null=True, blank=True, on_delete=models.CASCADE, default=None)
    category = models.ForeignKey(Category, default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name="posts")

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to="blog/posts/", null=True, blank=True)
    private = models.BooleanField(default=None)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title