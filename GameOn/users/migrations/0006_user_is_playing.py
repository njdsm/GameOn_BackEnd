# Generated by Django 3.2.4 on 2021-07-06 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_playing',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
