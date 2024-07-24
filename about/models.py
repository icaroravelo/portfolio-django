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
    avatar1 = models.URLField(max_length=500, blank=True)
    avatar2 = models.URLField(max_length=500, blank=True)
    stacks = models.ManyToManyField('Stack', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = 'about'	

    def __str__(self):
        return self.role

class Stack(models.Model):
    name = models.CharField(max_length=250)
    short_description = models.TextField('', blank=True, null=True)
    logo = models.URLField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Experience(models.Model):
    name = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    description = models.TextField('description', blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    country = models.CharField(max_length=250, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    is_currently = models.BooleanField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    logo = models.URLField(max_length=500, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def is_currently_working(self, end_date):
        if self.is_currently:
            return self.started_at.strftime('%d/%m/%Y') if self.started_date else end_date

    def __str__(self):
        return self.name