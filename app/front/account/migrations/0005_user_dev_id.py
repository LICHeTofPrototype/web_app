# Generated by Django 2.2.10 on 2020-03-28 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200326_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dev_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='dev_id'),
        ),
    ]
