# __author__ == 'jakey'

from django.contrib import admin
from common.models import ProvinceCity


@admin.register(ProvinceCity)
class ProvinceCityAdmin(admin.ModelAdmin):
    fields = ("name", "pid")
    search_fields = ("name", )
    list_display = ["name", "pid", "id"]
    list_filter = ["name"]
    list_per_page = 50
