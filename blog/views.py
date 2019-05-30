from django.shortcuts import render
from .models import Blog, Blog_comment


def blogs(request):
    all_blogs = Blog.objects.order_by('pub_date')
    return render(request, 'blog/blogs.html', {'all_blogs': all_blogs})


def single_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog/single_blog.html', {'blog': blog})
