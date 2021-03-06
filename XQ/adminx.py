import xadmin
from .models import Theme, XQ

class ThemeAdmin(object):
    list_display = ["title", "title2", "image", "add_time"]
    search_fields = ["title", "title2", "image"]
    list_filter = ["title", "title2", "image", "add_time"]
    style_fields = {"detail": "ueditor"}

xadmin.site.register(Theme, ThemeAdmin)

class XQAdmin(object):
    list_display = ["title", "add_time"]
    search_fields = ["title"]
    list_filter = ["title", "add_time"]
    style_fields = {"detail": "ueditor"}

xadmin.site.register(XQ, XQAdmin)