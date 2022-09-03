from django.shortcuts import render, HttpResponse
from django.http.response import JsonResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json
from utils.upload import  upload
import re
# Create your views here.


def article(request, id):
    article = Article.objects.get(id=id)
    toc_re = re.compile('##.+')
    toc_lis = toc_re.findall(article.content.__str__())
    toc_list = []
    for toc in toc_lis:
        toc_list.append({'toc_name':toc.replace('#', '')[1:], 'toc_count': '-' * toc.count('#')})
    article.viewed()
    comments = Comment.objects.filter(article=article)
    return render(request, 'article/article.html', locals())


def category(request, id):
    category = Category.objects.get(id=id)
    articles = Article.objects.filter(category=category)
    return render(request, 'article/category.html', locals())


def all_articles(request):
    articles = Article.objects.all()
    return render(request, 'article/all_articles.html', locals())


@login_required()
def new_article(request):
    if request.is_ajax():
        if request.POST:
            title = request.POST.get('title', '')
            if not title:
                return HttpResponse(json.dumps({'message': '请输入标题！'}))

            category = request.POST.get('category', '')
            if not category:
                return HttpResponse(json.dumps({'message': '请选择分类！'}))

            content = request.POST.get('content', '')
            if not content:
                return HttpResponse(json.dumps({'message': '请输入正文！'}))

            author = request.user
            x = Article(title=title, category_id=category,content_text=content ,content=content, author=author)
            x.save()
            return HttpResponse(json.dumps({'status': 1, 'message': '提交成功，3秒后跳转到文章页面', 'articleId':x.id}))
    return render(request, 'article/new_article.html', locals())


def search_article(request):
    q = request.GET.get('q', None)
    articles = Article.objects.filter(Q(title__icontains=q) | Q(content_text__icontains=q))
    article_len = len(articles)
    for article in articles:
        x = re.compile(f'.+{q}.+')
        try:
            article.content = x.findall(article.content)[0]
        except:
            pass
    return render(request, 'article/search_results.html', locals())


@login_required()
def comment_commit(request):
    if request.is_ajax():
        if request.POST:
            comment_content = request.POST.get('comment_content', None)
            if comment_content is None:
                return HttpResponse(json.dumps({'message': '请填写评论内容'}))

            article_id = request.POST.get('article_id', None)
            if article_id is None:
                return HttpResponse(json.dumps({'message': '非法请求'}))

            Comment(comment=comment_content, article_id=article_id, user_name=request.user).save()
            return HttpResponse(json.dumps({'status': 1, 'message': '评论成功！正在刷新页面'}))


@csrf_exempt
def upload_img(request):
    request =request
    url = upload('media', request.FILES.get('editormd-image-file', None))
    result = {"success": 1, "message": "图片上传成功", "url": url}
    return JsonResponse(result)