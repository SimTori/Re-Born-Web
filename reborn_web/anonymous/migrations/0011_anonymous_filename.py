# Generated by Django 3.0.2 on 2020-03-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anonymous', '0010_auto_20200311_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='anonymous',
            name='filename',
            field=models.CharField(max_length=64, null=True, verbose_name='이미지첨부파일명'),
        ),
    ]
