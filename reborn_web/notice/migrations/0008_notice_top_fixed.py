# Generated by Django 3.0.2 on 2020-01-28 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0007_auto_20200128_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='top_fixed',
            field=models.NullBooleanField(verbose_name='상단고정'),
        ),
    ]