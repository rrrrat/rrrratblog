# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   rrrratblog  
@FileName       :   urls.py
@Author         :   tangchaolizi
@Datetime       :   2021/8/23 12:48 下午
@Software       :   PyCharm
@Show           :
"""
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'accounts'
urlpatterns = [
    path('login.html', views.sign_in, name='login'),  # 用户登录
    path('register.html', views.sign_up, name='register'),  # 用户登录
    path('logout.html', views.sign_out, name="logout"),  # 用户登出
    path('profile_edit.html', TemplateView.as_view(template_name='accounts/profile_edit.html'), name="profile_edit"),  # 用户登出
    path('save_profile_edit.html', views.save_profile_edit, name="save_profile_edit"),  # 用户登出
    path('upload_photo.html', TemplateView.as_view(template_name='accounts/upload_photo.html'), name='upload_photo'), # 头像上传主视图
    path('save_upload_photo.html', views.save_upload_photo, name="save_upload_photo"),  # 用户登出
]