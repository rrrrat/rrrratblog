# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   rrrratblog  
@FileName       :   menu_var.py
@Author         :   tangchaolizi
@Datetime       :   2021/8/23 5:08 下午
@Software       :   PyCharm
@Show           :
"""
from article.models import Category


def category(request):
    categorys = [category for category in Category.objects.all()]
    return {'categorys': categorys}