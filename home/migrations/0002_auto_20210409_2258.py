# Generated by Django 3.1.2 on 2021-04-09 22:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecategory',
            name='createdTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 9, 22, 58, 0, 810602)),
        ),
    ]
