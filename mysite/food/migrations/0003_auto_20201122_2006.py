# Generated by Django 3.1.1 on 2020-11-22 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20201113_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='food_img',
        ),
        migrations.AddField(
            model_name='food',
            name='food_img_url',
            field=models.TextField(null=True),
        ),
    ]