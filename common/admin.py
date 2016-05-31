# __author__ == 'jakey'

from django.contrib import admin
from common.models import ProvinceCity, ScenicStyle


@admin.register(ProvinceCity)
class ProvinceCityAdmin(admin.ModelAdmin):
    fields = ("name", "pid")
    search_fields = ("name", )
    list_display = ["name", "pid", "id"]
    list_filter = ["name"]
    list_per_page = 50


@admin.register(ScenicStyle)
class ScenicStyleAdmin(admin.ModelAdmin):
    list_display = ("style_name", "style_describe", "id", )
