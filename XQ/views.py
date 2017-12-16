from django.shortcuts import render
from .models import Theme, XQ
from Goods.models import Kind
from Base.models import Side, Bow, Tabbar


def xq(request):
    all_Themes = Theme.objects.all()
    all_Kinds = Kind.objects.all()
    all_XQs = XQ.objects.all()
    all_Bows = Bow.objects.all()
    all_Sides = Side.objects.all()
    all_Tabbars = Tabbar.objects.all()
    context = {
        "all_Themes": all_Themes,
        "all_Kinds": all_Kinds,
        "all_Bows": all_Bows,
        "all_Sides": all_Sides,
        "all_Tabbars": all_Tabbars,
        "all_XQs": all_XQs
     }
    return render(request, "xq.html", context)