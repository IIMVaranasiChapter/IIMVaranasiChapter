# Generated by Django 2.0.1 on 2018-02-04 09:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iimv', '0008_auto_20180204_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='updates',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 4, 15, 24, 6, 972509)),
        ),
    ]
