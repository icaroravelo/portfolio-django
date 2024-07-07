from django.db import models
from django.utils.text import slugify

# Create your models here.
class Tag(models.Model):
    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

    def __str__(self):
        return self.title

class Post(models.Model):
    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/images', blank=True, null=True)
    author = models.CharField(max_length=100)
    categories = models.ManyToManyField("Tag", related_name="posts")
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

