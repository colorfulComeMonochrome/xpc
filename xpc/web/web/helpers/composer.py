from web.models.copyright import Copyright
from web.models.post import Post


def get_posts_by_cid(cid, num=2):
    cr_list = Copyright.objects.filter(cid=cid)[:num]
    posts = []
    for cr in cr_list:
        post = Post.objects.filter(pid=cr.pid)
        posts.append(post)
    return posts


def get_role_in_post(pid, cid):
    cr = Copyright.objects.filter(pid=pid, cid=cid).first()
    return cr.roles








