from django.db import models

# Create your models here.
import datetime
import os


class Conf(models.Model):
    main_website = models.CharField(max_length=64, verbose_name='主网站', default="rrrrat.com")
    title = models.CharField(max_length=20, verbose_name='标题', default="rrrrat'blog")
    website_number = models.CharField(max_length=100, verbose_name='备案号', default='京ICP备2020034849号-1')
    website_logo = models.ImageField(upload_to='logo', verbose_name='网站logo', default='')