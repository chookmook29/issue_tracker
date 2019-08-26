from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Blog, BlogComment
from .forms import BlogCommentForm
from users.models import CustomUser


def blogs(request):
    all_blogs = Blog.objects.order_by("pub_date")
    return render(request, "blogs.html", {"all_blogs": all_blogs})


def single_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    comment_list = (
        BlogComment.objects.select_related().filter(blog_id=pk).order_by("-date")
    )
    paginator = Paginator(comment_list, 4)
    page = request.GET.get("page")
    comments = paginator.get_page(page)
    return render(request, "single_entry.html", {"blog": blog, "comments": comments})


def blog_comment(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.author = request.user
            comment.save()
            user = CustomUser.objects.get(username=request.user)
            user.amount_comments += 1
            user.save()
            messages.success(request, ("Comment added!"))
            return redirect("single_blog", pk=pk)
    else:
        form = BlogCommentForm()
    return render(request, "blog_comment.html", {"form": form})
