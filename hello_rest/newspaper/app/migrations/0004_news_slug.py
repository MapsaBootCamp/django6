# Generated by Django 4.0.1 on 2022-01-21 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_news_author_news_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]