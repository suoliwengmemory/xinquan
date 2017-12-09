import xadmin
from .models import Contact, Theme

class ThemeAdmin(object):
    list_display = ["image", "add_time"]
    search_fields = ["image"]
    list_filter = ["image", "add_time"]

xadmin.site.register(Theme, ThemeAdmin)



class ContactAdmin(object):

    list_display = ["content1", "content2", "content3", "add_time"]
    search_fields = ["content1", "content2", "content3"]
    list_filter = ["content1", "content2", "content3", "add_time"]
xadmin.site.register(Contact, ContactAdmin)