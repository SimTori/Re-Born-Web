# Generated by Django 3.0.2 on 2020-03-03 18:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0008_auto_20200303_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calender',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 3, 23, 40, 40, 247725, tzinfo=utc), verbose_name='수정일'),
        ),
    ]
