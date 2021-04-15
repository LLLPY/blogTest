from random import choices
from captcha.image import ImageCaptcha
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django_redis import get_redis_connection
from app.models import User
from django.contrib.auth import authenticate  # 系统自带的验证方法
from django.contrib.auth import login


# 测试
def hello(request):
    return HttpResponse('hello world!')


# 定义一个注册视图类
class RegisterView(View):
    def get(self, request):
        # print('通过注册类视图实现')
        return render(request, 'register.html')

    # 执行注册
    def post(self, request):
        verifyCode = request.POST.get('verifyCode').lower().strip()
        # 检测验证码是否正确
        redis_con = get_redis_connection('default')  # 连接redis
        uuid = request.META['REMOTE_ADDR']  # 将ip作为用户的唯一标识
        thisVerifyCode = str(redis_con.get(uuid)).replace('b', '').replace('\'', '')
        if verifyCode != thisVerifyCode:
            return JsonResponse({'msg': '验证码错误!'})
        account = request.POST.get('account')
        isUserObj = User.objects.filter(username=account)

        # 如果验证码正确
        # 1.检测该账号是否已经注册
        if isUserObj.exists():
            return JsonResponse({'msg': '该账号已被注册!'})
        newUserObj = User()
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        if password != confirmPassword:
            return JsonResponse({'msg': '两次密码输入不一致!'})

        newUserObj.username = account
        newUserObj.password = password
        newUserObj.save()
        return JsonResponse({'msg': '注册成功!'})


# 图片验证码的视图类
class ImageCodeView(View):
    def get(self, request):
        ''':arg
        1.接受前端传过来的uuid(用户的唯一标识)
        2.判断uuid是否获取到
        3.通过调用captcha来生成图片验证码(图片二进制和图片内容)
        4.将图片内容保存到redis中
            uuid作为key,图片内容作为value,同时需要设置一个时效
        5.返回二进制图片给前端
        '''
        # 1.接受前端传过来的uuid(用户的唯一标识)
        # uuid=request.GET.get('uuid')
        # 2.判断uuid是否获取到
        # if uuid is None:
        #     return HttpResponseBadRequest('没有传递uuid')
        # 3.通过调用captcha来生成图片验证码(图片二进制和图片内容)
        imgCode, imge = self.returnRandomChars()
        uuid = request.META['REMOTE_ADDR']  # 将ip作为用户的唯一标识
        print('uuid:', uuid)
        print('verifyCode:', imgCode)
        # 4.将图片内容保存到redis中
        #     uuid作为key,图片内容作为value,时效300秒
        redis_con = get_redis_connection('default')  # 连接redis
        redis_con.setex(uuid, 300, imgCode.lower().strip())

        # 5.返回二进制图片给前端
        return HttpResponse(imge, content_type='image/jpeg')

    # 定义一个返回任意字符的函数,用于生成图片验证码的内容
    def returnRandomChars(self):
        charList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        imgCode = ''.join(choices(charList, k=4))  # 任意的4位字符
        img = ImageCaptcha()
        image = img.generate_image(imgCode)
        image.save('test.png')
        content = None  # 验证码的内容 (二进制文件)
        with open('test.png', 'rb') as f:
            content = f.read()
        return imgCode, content


# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        account = request.POST.get('account')
        print(account)
        return HttpResponse("1111")


# 登录
def _login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')
        isUserObj = User.objects.filter(username=account)
        # 检测该账号是否已经注册
        if not isUserObj.exists():  # JsonResponse({'msg':'该账号还未注册!'})
            response = render(request, 'login.html', context={'account': account})
            response.write("<script>window.onload=function(){alert('该账号还未注册!');}</script>")
            return response

        verifyUser = isUserObj.filter(password=password)
        if not verifyUser.exists():
            response = render(request, 'login.html', context={'account': account})
            response.write("<script>window.onload = function(){alert('密码错误!');}</script>")
            return response
        response = redirect(reverse('aaa:index'))
        response.set_cookie('is_login', True)  # 登录状态
        response.set_cookie('username', verifyUser.first().username, max_age=7 * 24 * 3600)  # 7天过期时间
        # 保持登录
        login(request, verifyUser.first())  # 使用django内置的login方法保持登录状态
        remember = request.POST.get('remember')
        remember = 'off'
        if remember == 'on':
            response.set_cookie('is_login', True, max_age=7 * 24 * 3600)
            request.session.set_expiry(None)  # 默认是记住两周
        else:
            request.session.set_expiry(0)  # 浏览器关闭后就过期

        return response


# 主页
def index(request):
    if request.method == 'GET':
        try:
            user = request.user
            avatar = user.avatar
            # 如果用户没有上传头像,使用系统默认头像
            if not avatar:
                avatar = 'imgs/test.jpg'
            context = {
                'avatar': str(avatar).replace('static/', '')

            }
            return render(request, 'index.html', context=context)

        except:
            return render(request, 'index.html')
