from django.db import models
from django.utils.text import slugify
import uuid
from about.models import Stack

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250, blank=True, null=True) # To create a slug
    slug = models.SlugField(blank=True, null=True, unique=True)
    short_description = models.TextField(blank=True, null=True)
    thumbnail = models.URLField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title 

class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField('', blank=True, null=True)
    thumbnail = models.URLField(max_length=500, blank=True)
    stacks = models.ManyToManyField(Stack, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    github_link = models.URLField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    contributor = models.ManyToManyField('Contributor', blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def featuring(self, is_featured):
        if is_featured:
            self.is_featured = True
            return ('Com participação de: {}'.format(', '.join([contributor.name for contributor in self.contributor.all()])))
        else:
            self.is_featured = False

    def __str__(self):
        return self.title

class Contributor(models.Model):
    name = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    thumbnail = models.URLField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name