from hashlib import md5
from django.utils.functional import cached_property
from web.models.post import Post
from django.core.paginator import Paginator
from django.shortcuts import render
from django.core.cache import cache
from web.models.comment import Comment
from web.helpers.composer import get_posts_by_cid
from django.views.decorators.cache import cache_page


# 让分页器从缓存中读取数据总条数  避免遍历整个数据库表
@cached_property
def count(self):
    # 多个地方用了分页器: 主页的作品列表  视频页里的评论列表
    # 通过sql语句并md5  使每个分页区分开  不会混淆
    sql, params = self.object_list.query.sql_with_params()
    sql = sql % params
    cache_key = md5(sql.encode('utf-8')).hexdigest()
    # print(cache_key)
    row_count = cache.get(cache_key)
    if not row_count:
        row_count = self.object_list.count()
        cache.set(cache_key, row_count)
    return row_count


Paginator.count = count


# @cache_page(60 * 15)
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
    first_composer = post.composers[0]
    first_composer.posts = get_posts_by_cid(first_composer.cid, 6)
    return render(request, 'post.html', locals())


def get_comments(request):
    pid = request.GET.get('id')
    # print(pid)
    page = request.GET.get('page')
    # print(page)
    comment_list = Comment.objects.filter(pid=pid).order_by('-created_at')
    paginator = Paginator(comment_list, 10)
    comments = paginator.page(page)
    print(comments)
    print(comment_list)
    return render(request, 'comments.html', locals())





