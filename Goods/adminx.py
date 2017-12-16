import xadmin
from .models import Product, Theme, Kind


class ThemeAdmin(object):
    list_display = ["title", "title2", "image", "add_time"]
    search_fields = ["title", "title2", "image"]
    list_filter = ["title", "title2", "image", "add_time"]
    style_fields = {"detail": "ueditor"}
xadmin.site.register(Theme, ThemeAdmin)


class KindAdmin(object):
    list_display = ["name", "add_time"]
    search_fields = ["name"]
    list_filter = ["name", "add_time"]
xadmin.site.register(Kind, KindAdmin)


class ProductAdmin(object):
    list_display = ["kind", "title", "show", "image", "image1", "image2", "image3", "image4", "image5", "add_time"]
    search_fields = ["kind", "title", "show", "image", "image1", "image2", "image3", "image4", "image5"]
    list_filter = ["kind", "title", "show", "image", "image1", "image2", "image3", "image4", "image5", "add_time"]
    style_fields = {"detail": "ueditor"}
xadmin.site.register(Product, ProductAdmin)

