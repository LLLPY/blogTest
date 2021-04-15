# Generated by Django 3.1.2 on 2021-04-09 22:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('createdTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': '类别管理',
                'verbose_name_plural': '类别管理',
                'db_table': '文章分类',
            },
        ),
    ]