from django.utils.functional import cached_property
from web.models.post import Post
from django.core.paginator import Paginator
from django.shortcuts import render
from django.core.cache import cache
from web.models.comment import Comment
from web.helpers.composer import get_posts_by_cid
from django.views.decorators.cache import cache_page


@cached_property
def count(self):
    posts_count = cache.get('posts_count')
    if not posts_count:
        posts_count = self.object_list.count()
        cache.set('posts_count', posts_count)
    return posts_count


Paginator.count = count


@cache_page(60 * 15)
def show_list(request):
    post_list = Post.objects.order_by('-play_counts')
    paginator = Paginator(post_list, 40)
    posts = paginator.page(1)

    for post in posts:
        # print(post.get_composers())
        post.composers = post.get_composers()
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, pid):
    post = Post.get(pid=pid)
    post.composers = post.get_composers()
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





