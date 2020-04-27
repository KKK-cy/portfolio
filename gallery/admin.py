from django.contrib import admin

# Register your models here.
from gallery.models import Gallery

# 把功能模块在admin中注册一下
admin.site.register(Gallery)