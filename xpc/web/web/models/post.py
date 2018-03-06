import pickle
from django.db import models
from web.models.composer import Composer
from web.models.copyright import Copyright
from web.models import Model
from web.helpers import r


class Post(models.Model, Model):
    pid = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=256)
    thumbnail = models.CharField(max_length=512, blank=True, null=True)
    preview = models.CharField(max_length=512, blank=True, null=True)
    video = models.CharField(max_length=512, blank=True, null=True)
    video_format = models.CharField(max_length=32, blank=True, null=True)
    category = models.CharField(max_length=512)
    created_at = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    play_counts = models.IntegerField()
    like_counts = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'posts'

    # 已继承自Model中的get方法
    # @classmethod
    # def get(cls, pid):
    #     post = r.get('pid_%s' % pid)
    #     if post:
    #         return pickle.loads(post)
    #     post = Post.objects.get(pid=pid)
    #     r.set('post_%s' % pid, pickle.dumps(post))
    #     return post

# 优化前的get_composers
#     def get_composers(self):
#         """取出当前作品的所有作者"""
#
#         composers = []
#         # cr_list = Copyright.objects.filter(pid=self.pid).all()
#         cache_key = 'cr_pid_%s' % self.pid
#         # print(cache_key)
#         if r.exists(cache_key):
#             cr_list = [pickle.loads(i) for i in r.lrange(cache_key, 0, -1)]
#         else:
#             cr_list = Copyright.objects.filter(pid=self.pid).all()
#             r.lpush(cache_key, *[pickle.dumps(cr) for cr in cr_list])
#         # r.lpush('copyright_from_post_%s' % self.pid, cr_list)
#         for cr in cr_list:
#             # composer = r.get('composer_%s' % cr.cid)
#             composer = Composer.get(cid=cr.cid)
#             # if composer:
#             #     pass
#             #     # composer = pickle.loads(composer)
#             # else:
#             #     # composer = Composer.objects.filter(cid=cr.cid).first()
#             #     # r.set('composer_%s' % cr.cid, pickle.dumps(composer))
#             if composer:
#                 composer.role = cr.roles
#                 composers.append(composer)
#         return composers

    def get_composers(self):
        """取出当前作品的所有作者"""
        cache_key = 'cr_pid_%s' % self.pid
        composers = [pickle.loads(i) for i in r.lrange(cache_key, 0, -1)]
        if not composers:
            cr_list = Copyright.objects.filter(pid=self.pid).all()
            for cr in cr_list:
                composer = Composer.get(cid=cr.cid)
                if composer:
                    composer.role = cr.roles
                    composers.append(composer)
                    r.lpush(cache_key, pickle.dumps(composer))
        return composers

    @property
    def first_composer(self):
        return self.composers[0]





