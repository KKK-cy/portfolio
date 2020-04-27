# -*- coding: utf-8 -*-

"""
    # @Author : Administrator
    # @Time : 2020/4/27 19:25
    脚本说明：

"""
from django.shortcuts import render
from gallery.models import Gallery

""" 显示主页 """
def home(request):
    # 获取到作品集（所有的作品）
    gallery = Gallery.objects.all()
    # 在主页上显示作品的信息
    return render(request, 'home.html',{'gallery':gallery})
