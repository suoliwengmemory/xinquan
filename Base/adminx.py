import xadmin
from .models import Tabbar, Side ,Bow

class BowAdmin(object):
    list_display = ["title", "bar1", "bar2", "bar3", "bar4", "bar5", "bar6", "bar7", "image", "Telephone", "add_time"]
    search_fields = ["title", "bar1", "bar2", "bar3", "bar4", "bar5", "bar6", "bar7", "image", "Telephone"]
    list_filter = ["title", "bar1", "bar2", "bar3", "bar4", "bar5", "bar6", "bar7", "image", "Telephone", "add_time"]

xadmin.site.register(Bow, BowAdmin)

class SideAdmin(object):
    list_display = ["title", "bar", "bar1", "bar2", "bar3", "bar4", "bar5", "bar6", "bar7", "Telephone", "add_time"]
    search_fields = ["title", "bar", "bar1", "bar2", "bar3", "bar4", "bar5", "bar6", "bar7", "Telephone"]
    list_filter = ["title", "bar", "bar1", "bar2", "bar3", "bar4", "bar5", "bar6", "bar7", "Telephone", "add_time"]

xadmin.site.register(Side, SideAdmin)


class TabbarAdmin(object):
    list_display = ["title", "bar1", "bar2", "bar3", "bar4", "bar5", "bar6", "bar7", "image", "Telephone", "record", "add_time"]
    search_fields = ["title", "bar1", "bar2", "bar3", "bar4", "bar5", "bar6", "bar7", "image", "Telephone", "record"]
    list_filter = ["title", "bar1", "bar2", "bar3", "bar4", "bar5", "bar6", "bar7", "image", "Telephone", "record", "add_time"]

xadmin.site.register(Tabbar, TabbarAdmin)

