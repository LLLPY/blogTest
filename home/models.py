from django.db import models
from django.utils import timezone
from app.models import User

#博客类别
class ArticleCategory(models.Model):
    '''文章分类'''

    # 标题
    title = models.CharField(max_length=100, blank=True, db_column='标题')
    # 创建时间
    createdTime = models.DateTimeField(auto_now=True, db_column='创建时间')

    # admin站点显示,调查查看对象方便
    def __str__(self):
        return self.title

    class Meta:
        db_table = '文章分类'  # 修改表名
        verbose_name = '类别管理'  # admin站点显示
        verbose_name_plural = verbose_name

#博客
class Article(models.Model):
    # 作者
    author = models.ForeignKey(User, on_delete=models.CASCADE, db_column='作者')

    # 标题
    title = models.CharField(max_length=20, blank=True, db_column='标题')

    # 分类
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, db_column='分类')

    # 标签
    tags = models.CharField(max_length=50, blank=True, db_column='标签')

    # 摘要信息
    summary = models.CharField(max_length=200, null=False, blank=False, db_column='摘要信息')

    # 文章正文
    content = models.TextField(db_column='文章正文')

    # 浏览量
    total_views = models.PositiveIntegerField(default=0, db_column='浏览量')

    #获赞量
    total_likes=models.PositiveIntegerField(default=0,db_column='获赞量')

    # 不喜欢量
    total_nolikes = models.PositiveIntegerField(default=0, db_column='不喜欢量')

    # 评论量
    comments_count = models.PositiveIntegerField(default=0, db_column='评论量')

    # 文章创建时间
    createdTime = models.DateTimeField(default=timezone.now, db_column='文章创建时间')

    # 文章修改的时间
    updatedTime = models.DateTimeField(auto_now=True, db_column='文章修改的时间')  # 自动添加

    # 标题图 该图用于大厅页的展示 做多9张 9宫格
    avatar1 = models.ImageField(upload_to='static/article/%Y%m%d/', blank=True, db_column='标题图1')
    avatar2 = models.ImageField(upload_to='static/article/%Y%m%d/',null=True, blank=True, db_column='标题图2')
    avatar3 = models.ImageField(upload_to='static/article/%Y%m%d/',null=True, blank=True, db_column='标题图3')
    avatar4 = models.ImageField(upload_to='static/article/%Y%m%d/',null=True, blank=True, db_column='标题图4')
    avatar5 = models.ImageField(upload_to='static/article/%Y%m%d/',null=True, blank=True, db_column='标题图5')
    avatar6 = models.ImageField(upload_to='static/article/%Y%m%d/',null=True, blank=True, db_column='标题图6')
    avatar7 = models.ImageField(upload_to='static/article/%Y%m%d/',null=True, blank=True, db_column='标题图7')
    avatar8 = models.ImageField(upload_to='static/article/%Y%m%d/',null=True, blank=True, db_column='标题图8')
    avatar9 = models.ImageField(upload_to='static/article/%Y%m%d/',null=True, blank=True, db_column='标题图9')

    class Meta:
        db_table='博客' #修改表名
        ordering=('-createdTime',) #按照创建时间进行排序
        verbose_name='文章管理'
        verbose_name_plural=verbose_name

    def  __str__(self):

        return self.title