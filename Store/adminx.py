import xadmin
from .models import Store, Theme

class ThemeAdmin(object):
    list_display = ["title", "title2", "image", "add_time"]
    search_fields = ["title", "title2", "image"]
    list_filter = ["title", "title2", "image", "add_time"]
    style_fields = {"detail": "ueditor"}

xadmin.site.register(Theme, ThemeAdmin)


class StoreAdmin(object):
    list_display = ["title", "show", "image", "image1", "image2", "image3", "image4", "image5", "add_time"]
    search_fields = ["title", "show", "image", "image1", "image2", "image3", "image4", "image5"]
    list_filter = ["title", "show", "image", "image1", "image2", "image3", "image4", "image5", "add_time"]
    style_fields = {"detail": "ueditor"}
xadmin.site.register(Store, StoreAdmin)
