import xadmin
from .models import News, Theme


class ThemeAdmin(object):
    list_display = ["title", "title2", "image", "add_time"]
    search_fields = ["title", "title2", "image"]
    list_filter = ["title", "title2", "image", "add_time"]
    style_fields = {"detail": "ueditor"}

xadmin.site.register(Theme, ThemeAdmin)


class NewsAdmin(object):

    list_display = ["title", "image", "add_time"]
    search_fields = ["title", "image"]
    list_filter = ["title", "image", "add_time"]
    style_fields = {"detail": "ueditor"}
xadmin.site.register(News, NewsAdmin)

