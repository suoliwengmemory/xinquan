from django.shortcuts import render

from .models import Contact, Theme
from Goods.models import Kind
from Base.models import Side, Bow, Tabbar

def contact(request):
    all_Themes = Theme.objects.all()
    all_Contacts = Contact.objects.all()
    all_Kinds = Kind.objects.all()
    all_Bows = Bow.objects.all()
    all_Sides = Side.objects.all()
    all_Tabbars = Tabbar.objects.all()
    context = {
        "all_Contacts": all_Contacts,
        "all_Themes": all_Themes,
        "all_Bows": all_Bows,
        "all_Sides": all_Sides,
        "all_Tabbars": all_Tabbars,
        "all_Kinds": all_Kinds
    }
    return render(request, "contact.html", context)