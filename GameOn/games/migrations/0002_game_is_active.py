# Generated by Django 3.2.4 on 2021-07-05 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]