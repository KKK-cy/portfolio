from django.shortcuts import render

# Create your views here.
from blog.models import Blog


def blog_page(request):
    blogs = Blog.objects.all()
    return render(request,'blog.html',{'blogs':blogs})