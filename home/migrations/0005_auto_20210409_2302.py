# Generated by Django 3.1.2 on 2021-04-09 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210409_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecategory',
            name='createdTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
