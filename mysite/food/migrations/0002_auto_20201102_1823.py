# Generated by Django 3.1.2 on 2020-11-02 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='food_review_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='food_star',
            field=models.SmallIntegerField(default=0),
        ),
    ]
