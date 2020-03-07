# Generated by Django 3.0.4 on 2020-03-07 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PnnData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pnn_time', models.FloatField(verbose_name='pnn_time')),
                ('pnn', models.FloatField(verbose_name='pnn')),
                ('measurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.Measurement')),
            ],
        ),
    ]
