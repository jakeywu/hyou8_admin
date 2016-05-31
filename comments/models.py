# __author__ == 'jakey'

from django.db import models
from django.contrib.auth.models import User


class CommentScenic(models.Model):
    comments_title = models.CharField(verbose_name="评论主题", max_length=200, blank=True)
    scenic_id = models.ForeignKey("scenic.ScenicDescribe", verbose_name="景点ID", on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, verbose_name="用户ID", on_delete=models.CASCADE)
    picture_id = models.ForeignKey("user_info.UserPictures", verbose_name="图片ID", on_delete=models.CASCADE)
    pid = models.IntegerField(verbose_name="评论楼层", default=0)
    comments_content = models.TextField(verbose_name="评论内容")
    comments_like = models.IntegerField(verbose_name="点赞数", default=0)
    comments_view = models.IntegerField(verbose_name="查看数", default=0)

    def __str__(self):
        return self.comments_title

    class Meta:
        db_table = "comment_scenic"
        verbose_name = "用户评论表"
        verbose_name_plural = "用户评论表"
