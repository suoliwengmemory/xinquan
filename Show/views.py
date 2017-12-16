from django.shortcuts import render

from .models import Company, Theme
from Goods.models import Kind
from Base.models import Side, Bow, Tabbar

def show(request):
    all_Companys = Company.objects.all()
    all_Themes = Theme.objects.all()
    all_Kinds = Kind.objects.all()
    all_Bows = Bow.objects.all()
    all_Sides = Side.objects.all()
    all_Tabbars = Tabbar.objects.all()
    context = {
        "all_Themes": all_Themes,
        "all_Companys": all_Companys,
        "all_Bows": all_Bows,
        "all_Sides": all_Sides,
        "all_Tabbars": all_Tabbars,
        "all_Kinds": all_Kinds
    }
    return render(request, "show.html", context)


# def base(request):
#     all_Kinds = Kind.objects.all()
#
#     context = {
#         "all_Kinds": all_Kinds
#     }
#     return render(request, "base.html", context)