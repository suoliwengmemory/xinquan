import xadmin
from .models import Store, Theme

class ThemeAdmin(object):
    list_display = ["image", "add_time"]
    search_fields = ["image"]
    list_filter = ["image", "add_time"]

xadmin.site.register(Theme, ThemeAdmin)


class StoreAdmin(object):
    list_display = ["title", "show", "image", "image1", "image2", "image3", "image4", "image5", "detail", "add_time"]
    search_fields = ["title", "show", "image", "image1", "image2", "image3", "image4", "image5", "detail"]
    list_filter = ["title", "show", "image", "image1", "image2", "image3", "image4", "image5", "detail", "add_time"]
    style_fields = {"detail": "ueditor"}
xadmin.site.register(Store, StoreAdmin)
