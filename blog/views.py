from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Blog, Blog_comment


def blogs(request):
    all_blogs = Blog.objects.order_by('pub_date')
    return render(request, 'blogs.html', {'all_blogs': all_blogs})


def single_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    comment_list = Blog_comment.objects.select_related().filter(
                   ticket_id=pk).order_by('-date')
    paginator = Paginator(comment_list, 4)
    page = request.GET.get('page')
    comments = paginator.get_page(page)
    return render(request, 'single_entry.html', {'blog': blog, 'comments': comments})
