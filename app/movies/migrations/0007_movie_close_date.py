# Generated by Django 2.2.13 on 2020-07-01 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_merge_20200701_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='close_date',
            field=models.DateField(default='2020-08-31'),
        ),
    ]