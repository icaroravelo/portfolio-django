# Generated by Django 4.1.3 on 2024-06-25 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='stacks',
        ),
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
    ]
