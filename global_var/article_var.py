# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   rrrratblog  
@FileName       :   article_var.py
@Author         :   tangchaolizi
@Datetime       :   2021/8/23 6:00 下午
@Software       :   PyCharm
@Show           :
"""
from article.models import Article


def article_top(request):
    article_top = Article.objects.all()[:10]
    return {'article_top':article_top}
