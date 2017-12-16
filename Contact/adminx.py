import xadmin
from .models import Contact, Theme

class ThemeAdmin(object):
    list_display = ["title", "title2", "image", "add_time"]
    search_fields = ["title", "title2", "image"]
    list_filter = ["title",  "title2", "image", "add_time"]
    style_fields = {"detail": "ueditor"}
xadmin.site.register(Theme, ThemeAdmin)



class ContactAdmin(object):

    list_display = ["content1", "content2", "content3", "add_time"]
    search_fields = ["content1", "content2", "content3"]
    list_filter = ["content1", "content2", "content3", "add_time"]
xadmin.site.register(Contact, ContactAdmin)