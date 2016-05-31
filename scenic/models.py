# __author__ = 'jakey'

import os
import time
from uuid import uuid4
from django.db import models
from django.utils.timezone import now

PICTURES_CHOICES = (
    (1, '普通图片'),
    (2, '首页图片'),
    (3, '集邮图片'),
    (4, '内部路线图')
)


def image_uploads_path(instance, filename):
    cur_date = time.strftime("%Y-%m-%d").split("-")
    base_path = "pic/scenic/{0}/{1}/{2}".format(cur_date[0], cur_date[1], cur_date[2])
    extention = filename.split(".")[-1]
    if instance.pk:
        filename = '{0}.{1}'.format(instance.pk, extention)
    else:
        filename = '{0}.{1}'.format(uuid4().hex, extention)
    return os.path.join(base_path, filename)


def video_uploads_path(instance, filename):
    cur_date = time.strftime("%Y-%m-%d").split("-")
    base_path = "video/{0}/{1}/{2}".format(cur_date[0], cur_date[1], cur_date[2])
    extention = filename.split(".")[-1]
    if instance.pk:
        filename = '{0}.{1}'.format(instance.pk, extention)
    else:
        filename = '{0}.{1}'.format(uuid4().hex, extention)
    return os.path.join(base_path, filename)


class ScenicTopic(models.Model):
    """
    景区类型
    """
    topic_name = models.CharField(verbose_name="景区类型名称", max_length=100)
    topic_describe = models.CharField(verbose_name="类型描述", max_length=300, blank=True)

    def __str__(self):
        return self.topic_name

    class Meta:
        db_table = "scenic_types"
        verbose_name = "景区类型"
        verbose_name_plural = "景区类型"


class ScenicDescribe(models.Model):
    """
    景区主体
    """
    describe_name = models.CharField(verbose_name="景区名称", max_length=200)
    describe_alias = models.CharField(verbose_name="景区别名", max_length=200, blank=True)
    describe_overview = models.TextField(verbose_name="景区概述", blank=True)
    describe_detail = models.TextField(verbose_name="景区详细描述")
    describe_traffic = models.CharField(verbose_name="交通状况", max_length=300, blank=True)
    describe_open_time = models.CharField(verbose_name="景区开放时间", max_length=300, blank=True)
    describe_attention = models.CharField(verbose_name="景区注意事项", max_length=300, blank=True)
    describe_ticket_price = models.PositiveSmallIntegerField(verbose_name="景区门票价格", blank=True, default=0)
    describe_ticket_unit = models.CharField(verbose_name="景区门票单位", max_length=50, blank=True, default="人民币")
    describe_food = models.CharField(verbose_name="美食特产", max_length=500, blank=True)
    describe_cultural_folk = models.CharField(verbose_name="民俗文化", max_length=500, blank=True)
    describe_season = models.CharField(verbose_name="适合季节", max_length=200)
    describe_credential = models.CharField(verbose_name="景区资质", max_length=100, blank=True)
    describe_website = models.URLField(verbose_name="景区官网", blank=True)

    province_city = models.ForeignKey("common.ProvinceCity", verbose_name="景区省市")
    scenic_style_id = models.ForeignKey("common.ScenicStyle", verbose_name="景区风格ID")
    scenic_topic_id = models.ForeignKey("ScenicTopic", verbose_name="景区主题类型ID")

    def __str__(self):
        return self.describe_name

    class Meta:
        db_table = "scenic_describe"
        verbose_name = "景区主体"
        verbose_name_plural = "景区主体"


class ScenicPictures(models.Model):
    """
    景区关联图片
    """
    pictures_name = models.CharField(verbose_name="景区图片名称", max_length=200, blank=True)
    pictures_path = models.ImageField(verbose_name="景区图片路径", upload_to=image_uploads_path)
    pictures_type = models.PositiveSmallIntegerField(verbose_name="图片类型", choices=PICTURES_CHOICES, default=1)
    scenic_describe_id = models.ForeignKey("ScenicDescribe", verbose_name="景区名称", on_delete=models.CASCADE)

    def __str__(self):
        return self.pictures_name

    class Meta:
        db_table = "scenic_pictures"
        verbose_name = "图片维护"
        verbose_name_plural = "图片维护"


class ScenicVideos(models.Model):
    """
    景区关联视频
    """
    videos_name = models.CharField(verbose_name="景区视频名称", max_length=200, blank=True)
    videos_path = models.FileField(verbose_name="景区视频路径", upload_to=video_uploads_path)
    scenic_describe_id = models.ForeignKey("ScenicDescribe", verbose_name="景区名称", on_delete=models.CASCADE)

    def __str__(self):
        return self.videos_name

    class Meta:
        db_table = "scenic_videos"
        verbose_name = "视频维护"
        verbose_name_plural = "视频维护"


class ScenicNews(models.Model):
    """
    景区关联新闻
    """
    news_title = models.CharField(verbose_name="新闻标题", max_length=100)
    news_time = models.DateTimeField(verbose_name="新闻时间", default=now)
    news_abstract = models.CharField(verbose_name="新闻摘要", max_length=300)
    news_content = models.TextField(verbose_name="新闻内容")
    news_audit_status = models.NullBooleanField(verbose_name="审核状态")
    scenic_describe_id = models.ForeignKey("ScenicDescribe", verbose_name="景区名称", on_delete=models.CASCADE)

    def __str__(self):
        return self.news_title

    class Meta:
        db_table = "scenic_news"
        verbose_name = "景区新闻"
        verbose_name_plural = "景区新闻"
