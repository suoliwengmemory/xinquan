import xadmin
from .models import Product, Theme, Kind


class ThemeAdmin(object):
    list_display = ["image", "add_time"]
    search_fields = ["image"]
    list_filter = ["image", "add_time"]
xadmin.site.register(Theme, ThemeAdmin)


class KindAdmin(object):
    list_display = ["kind", "add_time"]
    search_fields = ["kind"]
    list_filter = ["kind", "add_time"]
xadmin.site.register(Kind, KindAdmin)


class ProductAdmin(object):
    list_display = ["type", "title", "show", "image", "detail", "add_time"]
    search_fields = ["type", "title", "show", "image", "detail"]
    list_filter = ["type", "title", "show", "image", "detail", "add_time"]
    style_fields = {"detail": "ueditor"}
xadmin.site.register(Product, ProductAdmin)

