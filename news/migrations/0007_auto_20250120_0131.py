# Generated by Django 3.1.14 on 2025-01-19 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_comentary'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='body_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='body_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='body_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='slug_en',
            field=models.TextField(max_length=350, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='slug_ru',
            field=models.TextField(max_length=350, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='slug_uz',
            field=models.TextField(max_length=350, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ru',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title_uz',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
