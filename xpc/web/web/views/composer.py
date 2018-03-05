from django.shortcuts import render
from web.models.composer import Composer
from web.models.copyright import Copyright
from web.helpers.composer import get_posts_by_cid


def oneuser(request, cid):
    composer = Composer.objects.get(cid=cid)
    cr_list = Copyright.objects.filter(cid=cid)
    posts = get_posts_by_cid(cid)
    return render(request, 'oneuser.html', locals())


def homepage(request, cid):
    composer = Composer.objects.get(cid=cid)
    cr_list = Copyright.objects.filter(cid=cid).all()
    composer.posts = get_posts_by_cid(cid)
    composer.rest_posts = composer.posts[1:]
    return render(request, 'homepage.html', locals())








