# __author__ == 'jakey'

from django.contrib import admin
from comments.models import CommentScenic


@admin.register(CommentScenic)
class CommentScenicAdmin(admin.ModelAdmin):
    pass
