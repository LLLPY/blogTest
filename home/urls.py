from django.conf.urls import url

from home import views
from app import views as appviews
from home.views import UserCenterView, writeBlogView

urlpatterns=[
    
    url(r'^home/',views.home,name='home'), #用户中心
    url(r'^logout/',views._logout,name='logout'), #退出
    url(r'^login/',appviews._login,name='login'), #登录
    url(r'^usercenter/',UserCenterView.as_view(),name='usercenter'), #用户中心(副本)
    url(r'^caogao/', views.caogao, name='caogao'), #草稿(用于测试)
    url(r'^index/', appviews.index, name='index'), #主页
    url(r'^writeBlog/',writeBlogView.as_view(),name='writeBlog'),#写博客

]