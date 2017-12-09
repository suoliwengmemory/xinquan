import xadmin
from .models import Index


class IndexAdmin(object):

    list_display = ["title", "high", "image", "add_time"]
    search_fields = ["title", "high", "image"]
    list_filter = ["title", "high", "image", "add_time"]
xadmin.site.register(Index, IndexAdmin)