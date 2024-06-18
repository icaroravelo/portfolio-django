from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    email = models.EmailField(("email"), max_length=254)
    bio = models.TextField('', blank=True, null=True)
    description = models.TextField('', blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    country = models.CharField(max_length=250, blank=True, null=True)
    avatar1 = models.ImageField(upload_to='about/avatars', blank=True)
    avatar2 = models.ImageField(upload_to='about/avatars', blank=True)
    stacks = models.ManyToManyField('Stack', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.role

class Stack(models.Model):
    name = models.CharField(max_length=250)
    short_description = models.TextField('', blank=True, null=True)
    logo = models.ImageField(upload_to='stack/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name