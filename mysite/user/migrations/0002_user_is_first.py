# Generated by Django 3.1.1 on 2020-11-12 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_first',
            field=models.BooleanField(default=True),
        ),
    ]
