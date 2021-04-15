from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

#定义用户模型
class User(AbstractUser): #模型继承自django自带的User模型 并在其基础上添加另外的属性


    #手机号
    mobile=models.CharField(max_length=11,unique=True,blank=False) #blank=True 表示必须要填写该字段的值

    #头像信息 头像的保存路径static/avatar/%Y%m%d
    avatar=models.ImageField(upload_to='static/avatar/%Y%m%d',blank=True) #blank=True 表示该字段的值可有可无

    #简介
    desc=models.CharField(max_length=500,blank=True)

    class Meta:
        db_table='User' #修改表名
        verbose_name='用户管理' #admin 后台显示
        verbose_name_plural=verbose_name

    #只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
    def __str__(self):
        return self.mobile