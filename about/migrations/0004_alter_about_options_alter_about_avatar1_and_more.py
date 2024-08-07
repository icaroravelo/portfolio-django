# Generated by Django 4.1.3 on 2024-07-07 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_remove_experience_stacks_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'about'},
        ),
        migrations.AlterField(
            model_name='about',
            name='avatar1',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='about',
            name='avatar2',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='experience',
            name='logo',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='stack',
            name='logo',
            field=models.URLField(blank=True, max_length=500),
        ),
    ]
