from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http.response import JsonResponse
from .models import Profile
import json
import uuid
import re
import base64
from utils.upload import upload

# Create your views here.


def sign_up(request):
    """
    用户注册
    """
    if request.user.is_authenticated:
        return redirect('/')
    if request.is_ajax():
        if request.POST:
            data = {}
            cdata = {}
            if request.POST['username']:
                username = request.POST['username']
                cdata['username'] = username
                if Profile.objects.filter(username=username):
                    data['message'] = '用户名已存在！请重新输入用户名！'
                    return HttpResponse(json.dumps(data))
            else:
                data['message'] = '请输入用户名！'
                return HttpResponse(json.dumps(data))

            if request.POST['password']:
                password = request.POST['password']
                cdata['password'] = password
            else:
                data['message'] = '请输入密码！'
                return HttpResponse(json.dumps(data))

            if request.POST['email']:
                email = request.POST['email']
                cdata['email'] = email
            else:
                data['message'] = '请输入邮箱！'
                return HttpResponse(json.dumps(data))

            if request.POST['qq']:
                qq = request.POST['qq']
                cdata['qq'] = qq

            new_user = Profile.objects.create_user(**cdata)
            new_user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            data['status'] = 1
            return HttpResponse(json.dumps(data))

    return render(request, 'accounts/sign_up.html', locals())


def sign_in(request):
    """
    用户登录
    """
    if request.user.is_authenticated:
        return redirect('/')
    name = "用户登录"
    if request.is_ajax():
        if request.POST:
            data = {}
            if request.POST['username']:
                username = request.POST['username']
            else:
                data['message'] = '请输入用户名！'
                return HttpResponse(json.dumps(data))

            if request.POST['password']:
                password = request.POST['password']
            else:
                data['message'] = '请输入密码！'
                return HttpResponse(json.dumps(data))

            try:
                user = authenticate(username=username, password=password)
                login(request, user)
                data['status'] = 1
                return HttpResponse(json.dumps(data))
            except Exception as Error:
                data['message'] = '用户名或密码错误！'
                return HttpResponse(json.dumps(data))

    return render(request, 'accounts/sign_in.html', locals())


def save_profile_edit(request):
    if request.is_ajax():
        if request.POST:
            blog_address = request.POST.get('blog_address', '')
            wechart = request.POST.get('wechart', '')
            sex = request.POST.get('sex', '')
            introduction = request.POST.get('introduction', '')
            qq = request.POST.get('qq', '')
            current_profile = Profile.objects.get(id=request.user.id)
            current_profile.blog_address = blog_address
            current_profile.wechart = wechart
            current_profile.sex_choice = sex
            current_profile.introduction = introduction
            current_profile.qq = qq
            current_profile.save()
            rdata = {'message': '修改成功！', 'status': 1}
            return HttpResponse(json.dumps(rdata))
        else:
            return HttpResponse('什么玩意？')
    else:
        return HttpResponse('什么玩意？')


def save_upload_photo(request):
    if request.is_ajax():
        if request.POST:
            avatar = request.POST.get('avatar', '')
            ines = avatar.split('base64,')
            imgData = base64.b64decode(ines[1])
            ines_str = ines[0].__str__()
            ines_type = ines_str.split('/')
            ines_type = ines_type[1][:-1]
            x = Profile.objects.get(id = request.user.id)
            x.avatar = upload('avatar', imgData, ines_type)
            x.save()
            rdata = {'message': '修改成功！', 'status': 1}
            return HttpResponse(json.dumps(rdata))
        else:
            return HttpResponse('什么玩意？')
    else:
        return HttpResponse('什么玩意？')


def sign_out(request):
    """
    用户退出
    """
    logout(request)
    return redirect('/')