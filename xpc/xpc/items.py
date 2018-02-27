# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class PostItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pid = Field()
    title = Field()
    thumbnail = Field()  # 缩略图
    preview = Field()  # 预览图
    video = Field()
    video_format = Field()  # 视频格式
    category = Field()  # 分类
    created_at = Field()
    play_counts = Field()  # 播放次数
    like_counts = Field()  # 被赞次数
    description = Field()  # 描述


class CommentItem(scrapy.Item):
    commentid = Field()  # 评论的id
    pid = Field()  # 被评论的电影的id
    cid = Field()  # 评论者id
    created_at = Field()  # 评论创建时间
    content = Field()  # 评论内容
    like_counts = Field()  # 被赞次数


# 用户
class ComposerItem(scrapy.Item):
    cid = Field()
    name = Field()
    banner = Field()  # 背景图片
    avatar = Field()  # 头像
    verified = Field()  # 是否经过验证
    intro = Field()  # 简介
    like_counts = Field()  # 点赞次数
    fans_counts = Field()  # 该用户的粉丝数
    follow_counts = Field()  # 该用户关注的人数

# 定位标签（导演，制作人等等）
class CopyrightItem(scrapy.Item):
    pcid = Field()
    pid = Field()
    cid = Field()  # 作者id
    roles = Field()
