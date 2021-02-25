# Generated by Django 3.1.4 on 2021-01-02 15:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20210102_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 15, 50, 7, 323739, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 15, 50, 7, 323283, tzinfo=utc)),
        ),
    ]
