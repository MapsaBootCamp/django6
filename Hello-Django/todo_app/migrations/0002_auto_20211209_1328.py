# Generated by Django 3.2.9 on 2021-12-09 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
