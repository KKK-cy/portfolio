# -*- coding: utf-8 -*-

"""
    # @Author : Administrator
    # @Time : 2020/4/27 21:50
    脚本说明：
        
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
import blog.views

urlpatterns = [
                  path('', blog.views.blog_page),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
