"""blogTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

#日志器的使用步骤
#1.导入logging包
import logging

#获取日志器
logger=logging.getLogger('djangoLog')
def log(request):
    #3.使用日志器记录信息
    logger.info('危险!!!') #信息内容由自己确定
    return HttpResponse('The test for logging.')



urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^app/',include(('app.urls','aaa'),namespace='aaa')),
    url('',include(('app.urls','aaa'),namespace='aaa')),
    url('',include(('home.urls','aaa'),namespace='home')),
    # url('',log),
]
