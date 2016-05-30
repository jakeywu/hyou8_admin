# __author__ == 'jakey'

import os
import time
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User


def user_image_path(instance, filename):
    cur_date = time.strftime("%Y-%m-%d").split("-")
    base_path = "pic/user/{0}/{1}/{2}".format(cur_date[0], cur_date[1], cur_date[2])
    extention = filename.split(".")[-1]
    if instance.pk:
        filename = '{0}.{1}'.format(instance.pk, extention)
    else:
        filename = '{0}.{1}'.format(uuid4().hex, extention)
    return os.path.join(base_path, filename)


class UserPictures(models.Model):
    """
    用户图片
    """
    user_pic_name = models.CharField(verbose_name="图片名称", max_length=200, blank=True)
    user_pic_path = models.ImageField(verbose_name="图片路径", upload_to=user_image_path)
    user_pic_type = models.PositiveSmallIntegerField(verbose_name="图片类型", default=1)
    user_id = models.ForeignKey(User, verbose_name="用户ID", on_delete=models.CASCADE)

    def __str__(self):
        return self.pictures_name

    class Meta:
        db_table = "user_pictures"
        verbose_name = "用户图片"
        verbose_name_plural = "用户图片"
