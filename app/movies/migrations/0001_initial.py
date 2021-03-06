# Generated by Django 2.2.14 on 2020-07-06 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_kor', models.CharField(max_length=100)),
                ('name_eng', models.CharField(max_length=100)),
                ('code', models.PositiveIntegerField()),
                ('running_time', models.DurationField(help_text='<분:초>로 입력 - 예시: 90:00 (90분)')),
                ('rank', models.IntegerField(unique=True)),
                ('acc_audience', models.PositiveIntegerField()),
                ('reservation_rate', models.FloatField()),
                ('open_date', models.DateField()),
                ('close_date', models.DateField(default='2020-08-31')),
                ('grade', models.CharField(choices=[('all', '전체관람가'), ('12+', '12세이상관람가'), ('15+', '15세이상관람가'), ('18+', '청소년관람불가')], max_length=20)),
                ('description', models.TextField(blank=True)),
                ('poster', models.ImageField(blank=True, upload_to='posters/')),
                ('trailer', models.FileField(blank=True, upload_to='trailers/')),
                ('actor', models.ManyToManyField(related_name='movies', to='movies.Actor')),
                ('director', models.ManyToManyField(related_name='movies', to='movies.Director')),
                ('genre', models.ManyToManyField(related_name='movies', to='movies.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('liked', models.BooleanField(default=False)),
                ('key_point', models.CharField(choices=[('actor', '배우'), ('prod', '연출'), ('story', '스토리'), ('visual', '영상미'), ('ost', 'OST')], max_length=20)),
                ('comment', models.TextField(blank=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='movies.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='liked',
            field=models.ManyToManyField(related_name='movies', through='movies.Rating', to=settings.AUTH_USER_MODEL),
        ),
    ]
