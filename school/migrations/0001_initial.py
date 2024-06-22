# Generated by Django 4.1.3 on 2024-06-22 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=250)),
                ('course', models.CharField(blank=True, max_length=250, null=True)),
                ('short_description', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, upload_to='school/logos')),
                ('certificate', models.ImageField(blank=True, upload_to='school/certicates')),
                ('started_at', models.DateField(blank=True, null=True)),
                ('is_finished', models.BooleanField(default=False)),
                ('finished_at', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
