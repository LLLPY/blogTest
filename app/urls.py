from django.conf.urls import url

from app import views

urlpatterns=[
    url(r'^hello/',views.hello,name='hello'),
    # url(r'^register/',views.register,name='register'),
    url(r'^register/',views.RegisterView.as_view(),name='register'),
    url(r'^login/',views._login,name='login'),
    url(r'^imgcode/',views.ImageCodeView.as_view(),name='imgcode'),
    url(r'^index/',views.index,name='index'),
]