from django.shortcuts import render

from .models import Company, Theme
from Goods.models import Kind


def show(request):
    all_Companys = Company.objects.all()
    all_Themes = Theme.objects.all()
    all_Kinds = Kind.objects.all()
    context = {
        "all_Themes": all_Themes,
        "all_Companys": all_Companys,
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