# Generated by Django 2.2.10 on 2020-03-28 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calc_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beatdata',
            name='measurement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.Measurement'),
        ),
        migrations.AlterField(
            model_name='pnndata',
            name='measurement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.Measurement'),
        ),
    ]