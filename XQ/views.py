from django.shortcuts import render
from .models import Theme
from Goods.models import Kind


def xq(request):
    all_Themes = Theme.objects.all()
    all_Kinds = Kind.objects.all()
    context = {
        "all_Themes": all_Themes,
        "all_Kinds": all_Kinds
     }
    return render(request, "xq.html", context)