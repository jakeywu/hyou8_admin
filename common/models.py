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
