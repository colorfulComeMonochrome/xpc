from web.models.composer import Composer
from web.models.copyright import Copyright
from web.models.post import Post


def get_posts_by_cid(cid):
    cr_list = Copyright.objects.filter(cid=cid)
    posts = []
    for cr in cr_list:
        post = Post.objects.filter(pid=cr.pid)
        posts.append(post)
    return posts

