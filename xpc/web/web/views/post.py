from web.models.post import Post
from django.core.paginator import Paginator
from django.shortcuts import render


def show_list(request):
    post_list = Post.objects.order_by('-like_counts')
    paginator = Paginator(post_list, 40)
    posts = paginator.page(1)
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, pid):
    post = Post.objects.get(pid=pid)
    return render(request, 'post.html', locals())











