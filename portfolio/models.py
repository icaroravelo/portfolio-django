from django.db import models
from about.models import Stack

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    short_description = models.TextField('', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='portfolio/categories/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField('', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='portfolio/projects/', blank=True)
    stacks = models.ManyToManyField(Stack, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
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
    thumbnail = models.ImageField(upload_to='portfolio/contributors/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name