# __author__ = 'jakey'

from django.contrib import admin
from scenic.models import ScenicDescribe, ScenicTopic, ScenicPictures, ScenicVideos, ScenicNews, ScenicStyle


@admin.register(ScenicDescribe)
class ScenicDescribeAdmin(admin.ModelAdmin):
    pass


@admin.register(ScenicTopic)
class ScenicTypesAdmin(admin.ModelAdmin):
    pass


@admin.register(ScenicPictures)
class ScenicPicturesAdmin(admin.ModelAdmin):
    pass


@admin.register(ScenicVideos)
class ScenicVideosAdmin(admin.ModelAdmin):
    pass


@admin.register(ScenicNews)
class ScenicNews(admin.ModelAdmin):
    pass


@admin.register(ScenicStyle)
class ScenicStyleAdmin(admin.ModelAdmin):
    pass
