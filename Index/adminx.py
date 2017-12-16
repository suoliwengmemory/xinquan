import xadmin
from .models import Index


class IndexAdmin(object):

    list_display = ["title", "high", "image", "url", "add_time"]
    search_fields = ["title", "high", "image", "url"]
    list_filter = ["title", "high", "image", "url", "add_time"]
xadmin.site.register(Index, IndexAdmin)