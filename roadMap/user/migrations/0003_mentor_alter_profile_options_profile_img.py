# Generated by Django 4.0 on 2021-12-14 14:49

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_profile_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user.profile')),
                ('major', models.CharField(choices=[('C', 'Computer Engineering'), ('E', 'Econimic'), ('P', 'Philosophy')], max_length=1)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('user.profile',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profile'},
        ),
        migrations.AddField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
    ]
