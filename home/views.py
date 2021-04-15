from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from app.models import User

#用户中心 继承django内置的LoginRequiredMixin类 用于判断用户是否处于登录状态
class UserCenterView(View,LoginRequiredMixin):
    def get(self,request):
        #获得用户的相关信息
        user=request.user
        print(3333,user.username)
        return render(request,'home.html')




#个人中心
def home(request):
    username = request.COOKIES.get('username')
    if username==None: #只有登录之后的用户才能访问该页面
        return redirect(reverse('aaa:login'))

    # 通过数据上传
    if request.method=='GET':
        avatar=''
        try:
            user=request.user
            avatar=user.avatar
        except:return redirect(reverse('aaa:login'))
        #如果用户没有上传头像,使用系统默认头像
        if not avatar:
            avatar='imgs/test.jpg'

        context={
            'avatar':str(avatar).replace('static/','')

        }
        return render(request, 'home.html',context=context)

    #修改图像
    if request.method=='POST':
        imgfile = request.FILES.get('imgfile')
        img = User.objects.filter(username=username).first()
        img.avatar = imgfile
        img.save()
        return HttpResponse('文件上传成功!')

#退出登录
def _logout(request):
    #调用系统内置的退出登录方法 删除session数据
    logout(request)
    #删除cookie数据
    response=redirect(reverse('home:home'))
    response.delete_cookie('is_login')
    response.delete_cookie('username')
    return response


#用于测试
def caogao(request):
    return render(request,'caogao.html')


#写博客
class writeBlogView(View,LoginRequiredMixin):

    def get(self,request):
        isLogin=request.COOKIES.get('is_login')
        username=request.COOKIES.get('username')
        print(username,isLogin)
        if not isLogin or not username: #如果没有登录的话就先登录
            return redirect(reverse('home:login'))

        avatar=User.objects.filter(username=username).first().avatar
        return render(request,'writeBlog.html',context={'avatar':str(avatar).replace('static/','')})



    def post(self,request):
        return


