from web.models.post import Post
from django.core.paginator import Paginator
from django.shortcuts import render
from web.models.comment import Comment
from web.helpers.composer import get_posts_by_cid


def show_list(request):
    post_list = Post.objects.order_by('-like_counts')
    paginator = Paginator(post_list, 40)
    posts = paginator.page(1)
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, pid):
    post = Post.objects.get(pid=pid)
    composer = post.first_composer
    composer.posts = get_posts_by_cid(composer.cid, 6)
    return render(request, 'post.html', locals())


def get_comments(request):
    pid = request.GET.get('id')
    print(pid)
    page = request.GET.get('page')
    print(page)
    comment_list = Comment.objects.filter(pid=pid).order_by('-created_at')
    paginator = Paginator(comment_list, 10)
    comments = paginator.page(page)
    print(comments)
    print(comment_list)
    return render(request, 'comments.html', locals())





