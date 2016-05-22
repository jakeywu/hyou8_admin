# __author__ = 'jakey'

from django.contrib import admin
from scenic.models import ProvinceCity, ScenicDescribe, ScenicTypes, ScenicPictures, ScenicVideos


@admin.register(ProvinceCity)
class ProvinceCityAdmin(admin.ModelAdmin):
    fields = ("name", "pid")
    search_fields = ("name", )
    list_display = ["name", "pid", "id"]
    list_filter = ["name"]
    list_per_page = 50


@admin.register(ScenicDescribe)
class ScenicDescribeAdmin(admin.ModelAdmin):
    pass


@admin.register(ScenicTypes)
class ScenicTypesAdmin(admin.ModelAdmin):
    pass


@admin.register(ScenicPictures)
class ScenicPicturesAdmin(admin.ModelAdmin):
    pass


@admin.register(ScenicVideos)
class ScenicVideosAdmin(admin.ModelAdmin):
    pass
