# Generated by Django 2.2.13 on 2020-07-04 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theaters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeatType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('impossible', '선택불가'), ('sit_apart', '띄어앉기석'), ('general', '일반'), ('disabled', '장애인석')], default='general', max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ['start_time']},
        ),
        migrations.RemoveField(
            model_name='seat',
            name='col',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='row',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='type',
        ),
        migrations.AddField(
            model_name='seat',
            name='name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='screen',
            name='seats_type',
            field=models.CharField(choices=[('0', 'type_0'), ('1', 'type_1'), ('2', 'type_2')], default='0', max_length=20),
        ),
        migrations.RemoveField(
            model_name='seat',
            name='screen',
        ),
        migrations.AddField(
            model_name='seat',
            name='screen',
            field=models.ManyToManyField(related_name='seats', through='theaters.SeatType', to='theaters.Screen'),
        ),
        migrations.AlterField(
            model_name='seatgrade',
            name='grade',
            field=models.CharField(choices=[('adult', '성인'), ('youth', '청소년'), ('preferred', '우대')], default='adult', max_length=10),
        ),
        migrations.AddField(
            model_name='seattype',
            name='screen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seat_types', to='theaters.Screen'),
        ),
        migrations.AddField(
            model_name='seattype',
            name='seat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seat_types', to='theaters.Seat'),
        ),
    ]