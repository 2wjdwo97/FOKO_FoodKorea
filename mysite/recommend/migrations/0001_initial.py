# Generated by Django 3.1.1 on 2020-11-11 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodRankCountry',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('rank', models.PositiveSmallIntegerField()),
                ('country_no', models.ForeignKey(db_column='country_no', on_delete=django.db.models.deletion.CASCADE, to='user.country')),
                ('food_no', models.ForeignKey(db_column='food_no', on_delete=django.db.models.deletion.CASCADE, to='food.food')),
            ],
            options={
                'db_table': 'data_food_rank_country',
            },
        ),
        migrations.CreateModel(
            name='FoodRankAge',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('age', models.PositiveSmallIntegerField()),
                ('rank', models.PositiveSmallIntegerField()),
                ('food_no', models.ForeignKey(db_column='food_no', on_delete=django.db.models.deletion.CASCADE, to='food.food')),
            ],
            options={
                'db_table': 'data_food_rank_age',
            },
        ),
    ]
