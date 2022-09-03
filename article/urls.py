# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   rrrratblog  
@FileName       :   urls.py
@Author         :   tangchaolizi
@Datetime       :   2021/8/23 4:30 下午
@Software       :   PyCharm
@Show           :
"""
from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'article'
urlpatterns = [
    path('<int:id>.html', views.article, name='article'),  # 文章内容
    path('category/<int:id>.html', views.category, name='category'),  # 文章分类
    path('all_articles.html', views.all_articles, name='all_articles'),  # 所有文章
    path('new_article.html', views.new_article, name='new_article'),  # 新建文章
    path('upload_img/', views.upload_img, name='upload_img'),  # 图片上传
    path('comment_commit/', views.comment_commit, name='comment_commit'),  # 评论提交
    path('search_article/', views.search_article, name='search_article'),  # 搜索文章
]