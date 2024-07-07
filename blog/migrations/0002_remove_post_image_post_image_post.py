# Generated by Django 4.1.3 on 2024-07-07 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image_post',
            field=models.URLField(blank=True, default='', max_length=500),
        ),
    ]
