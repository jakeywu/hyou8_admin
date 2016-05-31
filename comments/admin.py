# __author__ == 'jakey'

from django.contrib import admin
from comments.models import CommentScenic


@admin.register(CommentScenic)
class CommentScenicAdmin(admin.ModelAdmin):
    list_display = ("comments_title", "scenic_id", "user_id", "picture_id", "comments_like", "comments_view", )
