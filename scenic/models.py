# __author__ = 'jakey'

from django.db import models


class ProvinceCity(models.Model):
    name = models.CharField(verbose_name="国家-省-市", max_length=50)
    pid = models.IntegerField(verbose_name="父节点ID")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "province_city"
        verbose_name = "国家-省份-市"
        verbose_name_plural = "国家-省份-市"


class ScenicEntity(models.Model):
    pass
