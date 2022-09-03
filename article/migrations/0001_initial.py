# Generated by Django 3.2.5 on 2021-08-23 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='文章标题')),
                ('date_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('content', mdeditor.fields.MDTextField(blank=True, null=True, verbose_name='文章正文')),
                ('view', models.BigIntegerField(default=0, verbose_name='阅读数')),
                ('comment', models.BigIntegerField(default=0, verbose_name='评论数')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '博客文章',
                'verbose_name_plural': '博客文章',
                'ordering': ['-date_time'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='文章类型')),
                ('show', models.CharField(max_length=255, verbose_name='类型说明')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '文章类型',
                'verbose_name_plural': '文章类型',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=30, verbose_name='标签名称')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='评论时间')),
                ('comment', models.TextField(max_length=500, verbose_name='评论内容')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_id', to='article.article', verbose_name='文章')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论人')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'ordering': ['create_time'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='article.category', verbose_name='文章类型'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='article.Tag'),
        ),
    ]
