import xadmin
from .models import Theme

class ThemeAdmin(object):
    list_display = ["image", "add_time"]
    search_fields = ["image"]
    list_filter = ["image", "add_time"]

xadmin.site.register(Theme, ThemeAdmin)