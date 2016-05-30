# __author__ == 'jakey'

from django.contrib import admin
from user_info.models import UserPictures


@admin.register(UserPictures)
class UserPicturesAdmin(admin.ModelAdmin):
    pass
