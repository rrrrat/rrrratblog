from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    """
    用户信息表
    """
    moblie = models.CharField(null=True, max_length=255, verbose_name="电话号码")
    avatar = models.ImageField(upload_to='users_avatar', blank=True, default='/static/images/users/avatar-001.jpg',
                               verbose_name='用户头像')
    status = models.CharField(null=True, max_length=255, default=1, verbose_name="状态")
    sex_choice = ((0, '女性'), (1, '男性'))
    wechart = models.CharField(null=True, blank=True, max_length=50, default=1, verbose_name='微信')
    qq = models.CharField(null=True, blank=True, max_length=10,default=1, verbose_name='QQ')
    blog_address = models.CharField(null=True, blank=True, max_length=100, default='localhost', verbose_name='博客地址')
    introduction = models.TextField(blank=True, max_length=500, default='爸爸的爸爸是爷爷', verbose_name='自我介绍')
    value1 = models.CharField(null=True, max_length=255, default=1, verbose_name="value1")
    value2 = models.CharField(null=True, max_length=255, default=1, verbose_name="value2")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
