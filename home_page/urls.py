# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   rrrratblog  
@FileName       :   urls.py
@Author         :   tangchaolizi
@Datetime       :   2021/8/23 11:17 上午
@Software       :   PyCharm
@Show           :
"""
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'home_page'
urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),  # 首页
    path('timeline.html', TemplateView.as_view(template_name='timeline.html'), name='timeline'),  # 首页
]