# Generated by Django 3.1.2 on 2021-04-14 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0007_auto_20210409_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecategory',
            name='createdTime',
            field=models.DateTimeField(auto_now=True, db_column='创建时间'),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_column='标题', max_length=20)),
                ('tags', models.CharField(blank=True, db_column='标签', max_length=50)),
                ('summary', models.CharField(db_column='摘要信息', max_length=200)),
                ('content', models.TextField(db_column='文章正文')),
                ('total_views', models.PositiveIntegerField(db_column='浏览量', default=0)),
                ('total_likes', models.PositiveIntegerField(db_column='获赞量', default=0)),
                ('total_nolikes', models.PositiveIntegerField(db_column='不喜欢量', default=0)),
                ('comments_count', models.PositiveIntegerField(db_column='评论量', default=0)),
                ('createdTime', models.DateTimeField(db_column='文章创建时间', default=django.utils.timezone.now)),
                ('updatedTime', models.DateTimeField(auto_now=True, db_column='文章修改的时间')),
                ('avatar', models.ImageField(blank=True, db_column='标题图', upload_to='static/article/%Y%m%d/')),
                ('author', models.ForeignKey(db_column='作者', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(db_column='分类', on_delete=django.db.models.deletion.CASCADE, to='home.articlecategory')),
            ],
            options={
                'verbose_name': '文章管理',
                'verbose_name_plural': '文章管理',
                'db_table': '博客',
                'ordering': ('-createdTime',),
            },
        ),
    ]
