# __author__ == 'jakey'

from django.db import models
from django.contrib.auth.models import User


class CommentScenic(models.Model):
    scenic_id = models.ForeignKey("scenic.ScenicDescribe", verbose_name="景点ID", on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, verbose_name="用户ID", on_delete=models.CASCADE)
    pid = models.IntegerField(verbose_name="评论楼层", default=0)
    content = models.TextField(verbose_name="评论内容")

    def __str__(self):
        return self.scenic_id

    class Meta:
        db_table = "comment_scenic"
        verbose_name = "用户评论表"
        verbose_name_plural = "用户评论表"
