from django.db import models

# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=250)
    course = models.CharField(max_length=250, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='school/logos', blank=True)
    certificate = models.ImageField(upload_to='school/certicates', blank=True)
    started_at = models.DateField(blank=True, null=True)
    is_finished = models.BooleanField(default=False) # Status of the course
    finished_at = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def start_date_transform(self):
        return self.started_at.strftime('%d/%m/%Y') if self.started_at else 'Data não informada'

    def if_finished(self):
        if self.finished_at:
            return 'Concluído em: {}'.format(self.finished_at.strftime('%d/%m/%Y'))
        else:
            return 'Cursando'

    def __str__(self):
        return self.school_name