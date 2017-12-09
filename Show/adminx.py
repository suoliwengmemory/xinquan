import xadmin
from .models import Company,Theme


class ThemeAdmin(object):
    list_display = ["image", "add_time"]
    search_fields = ["image"]
    list_filter = ["image", "add_time"]

xadmin.site.register(Theme, ThemeAdmin)


class CompanyAdmin(object):

    list_display = ["title", "image", "detail", "add_time"]
    search_fields = ["title", "image", "detail"]
    list_filter = ["title", "image", "detail", "add_time"]
    style_fields = {"detail": "ueditor"}
xadmin.site.register(Company, CompanyAdmin)

