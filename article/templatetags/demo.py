# !/usr/anaconda3/bin python
# -*-coding:utf-8-*-
"""
@Project        :   rrrratblog  
@FileName       :   demo.py
@Author         :   tangchaolizi
@Datetime       :   2021/8/24 6:09 下午
@Software       :   PyCharm
@Show           :
"""
from django import template
import time


register = template.Library()


@register.filter
def dealwithtime(timeNum):
    timeStamp = float(timeNum / 1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y年%m月%d日", timeArray)
    return otherStyleTime
