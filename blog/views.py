from django.shortcuts import render
from .models import Blog


def blogs(request):
    entries = Blog.objects.order_by('pub_date')
    return render(request, 'blog/blogs.html', {'entries': entries})
