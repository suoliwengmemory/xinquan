from django.shortcuts import render, get_object_or_404

from .models import Lesson, Theme
from Goods.models import Kind
from Base.models import Side, Bow, Tabbar

def lesson(request):
    all_Lessons = Lesson.objects.all()
    all_Themes = Theme.objects.all()
    all_Kinds = Kind.objects.all()
    all_Bows = Bow.objects.all()
    all_Sides = Side.objects.all()
    all_Tabbars = Tabbar.objects.all()
    context = {
        "all_Themes": all_Themes,
        "all_Lessons": all_Lessons,
        "all_Bows": all_Bows,
        "all_Sides": all_Sides,
        "all_Tabbars": all_Tabbars,
        "all_Kinds": all_Kinds
    }
    return render(request, "lesson.html", context)