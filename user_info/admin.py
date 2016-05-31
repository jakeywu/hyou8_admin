# __author__ == 'jakey'

from django.contrib import admin
from user_info.models import UserPictures


@admin.register(UserPictures)
class UserPicturesAdmin(admin.ModelAdmin):
    list_display = ("user_pic_name", "user_pic_path", "user_pic_style", "user_id")
