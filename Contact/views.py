from django.shortcuts import render

from .models import Contact, Theme
from Goods.models import Kind

def contact(request):
    all_Themes = Theme.objects.all()
    all_Contacts = Contact.objects.all()
    all_Kinds = Kind.objects.all()
    context = {
        "all_Contacts": all_Contacts,
        "all_Themes": all_Themes,
        "all_Kinds": all_Kinds
    }
    return render(request, "contact.html", context)