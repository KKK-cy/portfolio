from django.shortcuts import render,get_object_or_404

# Create your views here.
from blog.models import Blog


def blog_page(request):
    blogs = Blog.objects.all()
    return render(request,'blog.html',{'blogs':blogs})

def blog_text(request,blog_id):
    # blogs = Blog.objects.all()
    blog = Blog.objects.get(pk = blog_id)
    return render(request,'blog_text.html',{'blog':blog})