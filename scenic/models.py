# __author__ = 'jakey'

from django.db import models


class ProvinceCity(models.Model):
    """
    景区国家省市地址
    """
    name = models.CharField(verbose_name="国家-省-市", max_length=50)
    pid = models.IntegerField(verbose_name="父节点ID")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "province_city"
        verbose_name = "国家-省份-市"
        verbose_name_plural = "国家-省份-市"


class ScenicTypes(models.Model):
    """
    景区类型列表
    """
    types_name = models.CharField(verbose_name="景区类型名称", max_length=200, blank=True)

    def __str__(self):
        return self.types_name

    class Meta:
        db_table = "scenic_types"
        verbose_name = "景区类型"
        verbose_name_plural = "景区类型"


class ScenicPictures(models.Model):
    """
    景区图片路径
    """
    pictures_name = models.CharField(verbose_name="景区图片名称", max_length=200, blank=True)
    pictures_path = models.URLField(verbose_name="景区图片路径")

    def __str__(self):
        return self.pictures_name

    class Meta:
        db_table = "scenic_pictures"
        verbose_name = "景区图片"
        verbose_name_plural = "景区图片"


class ScenicVideos(models.Model):
    videos_name = models.CharField(verbose_name="景区视频名称", max_length=200, blank=True)
    videos_path = models.URLField(verbose_name="景区视频路径")

    def __str__(self):
        return self.videos_name

    class Meta:
        db_table = "scenic_videos"
        verbose_name = "景区视频"
        verbose_name_plural = "景区视频"


class ScenicDescribe(models.Model):
    """
    景区实体信息
    """
    describe_name = models.CharField(verbose_name="景区名称", max_length=200)
    describe_alias = models.CharField(verbose_name="景区别名", max_length=500)
    describe_overview = models.TextField(verbose_name="景区概述")
    describe_detail = models.TextField(verbose_name="景区详细描述")
    describe_traffic = models.CharField(verbose_name="交通状况", max_length=300)
    describe_open_time = models.CharField(verbose_name="景区开放时间", max_length=300)
    describe_attention = models.CharField(verbose_name="景区注意事项", max_length=300)
    describe_ticket_price = models.PositiveSmallIntegerField(verbose_name="景区门票价格")
    describe_ticket_unit = models.CharField(verbose_name="景区门票单位", max_length=50)
    scenic_types = models.ForeignKey("ScenicTypes", verbose_name="景区类型ID")
    province_city = models.ForeignKey("ProvinceCity", verbose_name="景区省市", on_delete=models.CASCADE)

    def __str__(self):
        return self.describe_name

    class Meta:
        db_table = "scenic_describe"
        verbose_name = "景区实体"
        verbose_name_plural = "景区实体"
