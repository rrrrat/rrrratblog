from django.db import models
from mdeditor.fields import MDTextField
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Tag(models.Model):
    tag_name = models.CharField('标签名称', max_length=30)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name


class Article(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=200, verbose_name='文章标题')
    category = models.ForeignKey('Category', verbose_name='文章类型', on_delete=models.DO_NOTHING)
    date_time = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    content = MDTextField(blank=True, null=True, verbose_name='文章正文')
    content_text = models.TextField('文章正文TEXT', max_length=10000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.DO_NOTHING)
    view = models.BigIntegerField(default=0, verbose_name='阅读数')
    comment = models.BigIntegerField(default=0, verbose_name='评论数')
    tag = models.ManyToManyField(Tag)  # 标签

    class Meta:
        ordering = ['-date_time']  # 按时间降序
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name

    def viewed(self):
        """
        增加阅读数
        :return:
        """
        self.view += 1
        self.save(update_fields=['view'])

    def commenced(self):
        """
        增加评论数
        :return:
        """
        self.comment += 1
        self.save(update_fields=['comment'])

    def __str__(self):
        return self.title


class Category(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField('文章类型', max_length=30)
    show = models.CharField('类型说明', max_length=255)
    created_time = models.DateTimeField('创建时间', default=timezone.now)

    @staticmethod
    def fetch_all_category():
        """
        获取所有的分类
        :return:
        """
        all_category = Category.objects.all()
        return all_category

    class Meta:
        ordering = ['name']
        verbose_name = "文章类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Comment(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    article = models.ForeignKey('Article', related_name='article_id', verbose_name='文章', on_delete=models.CASCADE)
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='评论人', on_delete=models.CASCADE)
    create_time = models.DateTimeField('评论时间', default=timezone.now)
    comment = models.TextField('评论内容', max_length=500)

    class Meta:
        ordering = ['-create_time']
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.id