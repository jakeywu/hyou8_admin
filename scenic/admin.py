# __author__ = 'jakey'

from django.contrib import admin
from scenic.models import ScenicDescribe, ScenicTopic, ScenicPictures, ScenicVideos, ScenicNews


@admin.register(ScenicDescribe)
class ScenicDescribeAdmin(admin.ModelAdmin):
    list_display = ("describe_name", "describe_ticket_price", "describe_season", "describe_credential",
                    "describe_open_time", )


@admin.register(ScenicTopic)
class ScenicTopicAdmin(admin.ModelAdmin):
    list_display = ("topic_name", "topic_describe", "id", )


@admin.register(ScenicPictures)
class ScenicPicturesAdmin(admin.ModelAdmin):
    list_display = ("pictures_name", "pictures_path", "pictures_type", "scenic_describe_id")


@admin.register(ScenicVideos)
class ScenicVideosAdmin(admin.ModelAdmin):
    pass


@admin.register(ScenicNews)
class ScenicNews(admin.ModelAdmin):
    list_display = ("news_title", "news_time", "news_abstract", "news_content", "news_audit_status",
                    "scenic_describe_id", )
