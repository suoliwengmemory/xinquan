from django.shortcuts import render

from .models import Tabbar, Side, Bow
from Goods.models import Kind

def contact(request):
    all_Bows = Bow.objects.all()
    all_Sides = Side.objects.all()
    all_Tabbars = Tabbar.objects.all()
    context = {
        "all_Bows": all_Bows,
        "all_Sides": all_Sides,
        "all_Tabbars": all_Tabbars
    }
    return render(request, "base.html", context)