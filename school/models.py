from django.db import models

# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=250)
    short_description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='school/logos', blank=True)
    certificate = models.ImageField(upload_to='school/certicates', blank=True)
    started_at = models.DateField(blank=True, null=True)
    is_finished = models.BooleanField(default=False)
    finished_at = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def if_finished(self, is_finished):
        if is_finished == True:
            return ('Concluído em: {}'.format(self.finished_at))
        else:
            return ('Cursando!')

    def __str__(self):
        return self.school_name