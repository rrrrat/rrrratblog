# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   rrrratblog  
@FileName       :   base_var.py
@Author         :   tangchaolizi
@Datetime       :   2021/8/23 11:43 上午
@Software       :   PyCharm
@Show           :
"""

from home_page.models import Conf


def base_var(request):
    global_title = Conf.objects.get(id=1).title.__str__()
    website_number = Conf.objects.get(id=1).website_number.__str__()
    return {'global_title':global_title, 'website_number': website_number}
