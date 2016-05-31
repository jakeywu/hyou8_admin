# __author__ == 'jakey'

from django.db import models


class ProvinceCity(models.Model):
    """
    景区国家省市地址
    """
    name = models.CharField(verbose_name="国家-省-市", max_length=50)
    pid = models.IntegerField(verbose_name="父节点ID", default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "province_city"
        verbose_name = "地址维护"
        verbose_name_plural = "地址维护"


class ScenicStyle(models.Model):
    """
    景区风格
    """
    style_name = models.CharField(verbose_name="风格名称", max_length=100)
    style_describe = models.CharField(verbose_name="详细描述", max_length=500, blank=True)

    def __str__(self):
        return self.style_name

    class Meta:
        db_table = "scenic_style"
        verbose_name = "主题风格"
        verbose_name_plural = "主题风格"
